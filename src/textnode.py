from enum import Enum
from leafnode import LeafNode

TextType = Enum('TextType', ["TEXT", "BOLD", "ITALIC", "CODE", "LINK", "IMAGE"])

class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, node):
    return self.text == node.text and self.text_type == node.text_type and self.url == node.url

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
  if not isinstance(text_node.text_type, TextType):
    raise ValueError
  else:
    match text_node.text_type:
      case TextType.TEXT:
        return LeafNode(None, text_node.text)
      case TextType.BOLD:
        return LeafNode("B", text_node.text)
      case TextType.ITALIC:
        return LeafNode("i", text_node.text)
      case TextType.CODE:
        return LeafNode("code", text_node.text)
      case TextType.LINK:
        return LeafNode("", text_node.text, "href")
      case TextType.IMAGE:
        return LeafNode("img", "", {"src": "", "alt": ""})
