import unittest

from htmlnode import LeafNode 

class TestNodeleaf(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
    
    def test_to_html2(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just some text.")
        self.assertEqual(node.to_html(), "Just some text.")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_to_html_empty_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_none_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()