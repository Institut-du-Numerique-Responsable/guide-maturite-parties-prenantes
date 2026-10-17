-- Adapt the site Markdown to the PDF: line breaks inside table cells,
-- links between pages, criteria table column widths.

function RawInline(el)
  if el.format == "html" and el.text:match("^<br%s*/?>$") then
    return pandoc.LineBreak()
  end
end

-- Links to other pages of the site become internal links (anchor) or plain text.
function Link(el)
  local target = el.target
  if target:match("^https?://") or target:match("^mailto:") then
    return el
  end
  local anchor = target:match("#(.+)$")
  if anchor then
    el.target = "#" .. anchor
    return el
  end
  return el.content
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
