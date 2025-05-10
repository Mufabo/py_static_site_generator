import enum

BlockType = enum.Enum("BlockType", [
    "paragraph",
    "heading",
    "code",
    "quote",
    "unordered_list",
    "ordered_list",
])

def block_to_block_type(block: str) -> BlockType:
  if block[0] == "#":
    return BlockType.heading
  if block[:3] == "```" and block[-3:] == "```":
    return BlockType.code
  if all([x[0] == ">" for x in block.split("\n")]):
    return BlockType.quote
  if all([x[0:1] == "- " for x in block.split("\n")]):
    return BlockType.unordered_list
  ordered_list = True
  lines = len(block.split("\n"))
  for i in range(lines):
    ordered_list = ordered_list and lines[i].startswith(f"{i+1}. ")
  if ordered_list:
    return BlockType.ordered_list
  return BlockType.paragraph