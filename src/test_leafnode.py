from leafnode import LeafNode

import unittest

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
      node = LeafNode("p", "Hello, world!")
      self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_leaf_to_html_a(self):
      node = LeafNode("a", "Hello, world!")
      self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

  def test_leaf_to_html_p(self):
      node = LeafNode("div", "Hello, world!")
      self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

if __name__ == "__main__":
    unittest.main()