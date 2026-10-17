-- Adapt the site Markdown to the PDF: line breaks inside table cells,
-- links between pages, criteria table column widths.

function RawInline(el)
  if el.format == "html" and el.text:match("^<br%s*/?>$") then
    return pandoc.LineBreak()
  end
end

-- Links between site pages: keep the link when its anchor exists in the PDF,
-- otherwise keep only the text (MkDocs and pandoc build anchors differently,
-- e.g. accents, and Typst refuses links to missing labels).
local function local_links(doc)
  local ids = {}
  doc:walk({
    Header = function(h) ids[h.identifier] = true end,
    Span = function(sp) if sp.identifier ~= "" then ids[sp.identifier] = true end end,
  })
  return doc:walk({
    Link = function(el)
      local target = el.target
      if target:match("^%a[%w+.-]*:") then
        return el
      end
      local anchor = target:match("#(.+)$")
      if anchor and ids[anchor] then
        el.target = "#" .. anchor
        return el
      end
      return el.content
    end,
  })
end

-- Criteria tables: wide text column, narrow priority and weighting columns.
function Table(tbl)
  if #tbl.colspecs == 3 and pandoc.utils.stringify(tbl.head):match("total") then
    tbl.colspecs[1] = { pandoc.AlignLeft, 0.70 }
    tbl.colspecs[2] = { pandoc.AlignCenter, 0.13 }
    tbl.colspecs[3] = { pandoc.AlignCenter, 0.17 }
  else
    for i, spec in ipairs(tbl.colspecs) do
      tbl.colspecs[i] = { pandoc.AlignLeft, spec[2] }
    end
  end
  return tbl
end

return {
  { RawInline = RawInline, Table = Table },
  { Pandoc = local_links },
}
