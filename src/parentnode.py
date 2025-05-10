from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag == None:
      raise ValueError
    if self.children == None:
      raise ValueError("No children")
    prefix = f"<{self.tag}>"
    suffix = f"</{self.tag}>"
    child_html= "".join([c.to_html() for c in self.children])
    return prefix + child_html + suffix