-- Normalise le .docx FR : styles -> titres, tableaux -> cellules simples,
-- commentaires Word -> marqueurs ⟦Cn⟧ (traités ensuite à la main).
local level = { Style1 = 1, Style4 = 2, Style2 = 3, ["heading 1"] = 1 }
local notes = {}
local drop = { ["toc 1"] = true, ["TOC Heading"] = true }

function Div(el)
  local s = el.attributes["custom-style"]
  if not s then return nil end
  if drop[s] then return {} end
  local l = level[s]
  if l then
    local inl = pandoc.utils.blocks_to_inlines(el.content)
    if #pandoc.utils.stringify(inl):gsub("%s", "") == 0 then return {} end
    return pandoc.Header(l, inl)
  end
  return el.content
end

function Span(el)
  local id = el.attributes["comment-id"]
  if el.classes:includes("comment-start") then
    notes[id] = pandoc.utils.stringify(el.content)
    return pandoc.Str("⟦")
  end
  if el.classes:includes("comment-end") then
    return pandoc.Str("⟧{C" .. id .. ": " .. (notes[id] or "") .. "}")
  end
  if el.classes:includes("anchor") then return {} end
  return el.content
end

local function flatten(blocks)
  local out = pandoc.List()
  for i, b in ipairs(blocks) do
    if i > 1 then out:insert(pandoc.RawInline("html", "<br>")) end
    if b.t == "BulletList" or b.t == "OrderedList" then
      for j, item in ipairs(b.content) do
        if j > 1 then out:insert(pandoc.RawInline("html", "<br>")) end
        out:insert(pandoc.Str("•"))
        out:insert(pandoc.Space())
        out:extend(pandoc.utils.blocks_to_inlines(item))
      end
    else
      out:extend(pandoc.utils.blocks_to_inlines({ b }))
    end
  end
  return { pandoc.Plain(out) }
end

function Table(tbl)
  local function fix(rows)
    for _, row in ipairs(rows) do
      for _, cell in ipairs(row.cells) do
        cell.contents = flatten(cell.contents)
        cell.alignment = pandoc.AlignDefault
      end
    end
  end
  tbl.attr = pandoc.Attr()
  fix(tbl.head.rows)
  for _, body in ipairs(tbl.bodies) do fix(body.body) end
  for i, spec in ipairs(tbl.colspecs) do tbl.colspecs[i] = { pandoc.AlignDefault, nil } end
  return tbl
end

function Image(img)
  img.attributes = {}
  return img
end
