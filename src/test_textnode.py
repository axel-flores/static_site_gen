import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, url="http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, None)

        self.assertNotEqual(node, node2)
    
    def test_eq3(self):
        node = TextNode("This is a text node", TextType.LIST_ITEM, url="http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, None)

        self.assertNotEqual(node, node2)
    
    def test_eq4(self):
        node = TextNode("This is a text node", TextType.LIST_ITEM, url="http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, None)

        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")    

if __name__ == "__main__":
    unittest.main()