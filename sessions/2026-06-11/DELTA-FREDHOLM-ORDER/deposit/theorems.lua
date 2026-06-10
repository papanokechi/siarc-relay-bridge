-- Map fenced Divs with a theorem-like class to LaTeX amsthm environments.
-- Usage: pandoc ... --lua-filter=theorems.lua
local envs = {
  theorem = true, proposition = true, conjecture = true,
  remark = true, lemma = true, corollary = true, definition = true,
}
function Div(el)
  for _, cls in ipairs(el.classes) do
    if envs[cls] then
      local name = el.attributes["name"]
      local opener
      if name and #name > 0 then
        opener = "\\begin{" .. cls .. "}[" .. name .. "]"
      else
        opener = "\\begin{" .. cls .. "}"
      end
      local blocks = el.content
      table.insert(blocks, 1, pandoc.RawBlock("latex", opener))
      table.insert(blocks, pandoc.RawBlock("latex", "\\end{" .. cls .. "}"))
      return blocks
    end
  end
  return el
end
