from htmlnode import HTMLNode
import unittest


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value is None:
      raise ValueError
    elif self.tag is None:
      return self.value
    else:
      return f"<{self.tag}{"" if self.props is None else f'{self.props_to_html()}'}>{self.value}</{self.tag}>"
