import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "test div", None, {"div": "test div"})
        node2 = HTMLNode("p", "test div", None, {"div": "test div"})

        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode("div", "test div", None, {"div": "test div"})
        node2 = HTMLNode("div", "test div", None, {"div": "test div"})

        self.assertNotEqual(node, node2)
    
    def test_eq3(self):
        node = HTMLNode("div", "test div", None, {"div": "test div"})
        text1 = node.props_to_html()
        text2 = f"div=\"test div\""

        self.assertEqual(text1, text2)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    # def test_to_html_props(self):
    #     node = HTMLNode(
    #         "div",
    #         "Hello, world!",
    #         None,
    #         {"class": "greeting", "href": "https://boot.dev"},
    #     )
    #     self.assertEqual(
    #         node.props_to_html(),
    #         ' class="greeting" href="https://boot.dev"',
    #     )

    # def test_values(self):
    #     node = HTMLNode(
    #         "div",
    #         "I wish I could read",
    #     )
    #     self.assertEqual(
    #         node.tag,
    #         "div",
    #     )
    #     self.assertEqual(
    #         node.value,
    #         "I wish I could read",
    #     )
    #     self.assertEqual(
    #         node.children,
    #         None,
    #     )
    #     self.assertEqual(
    #         node.props,
    #         None,
    #     )

    # def test_repr(self):
    #     node = HTMLNode(
    #         "p",
    #         "What a strange world",
    #         None,
    #         {"class": "primary"},
    #     )
    #     self.assertEqual(
    #         node.__repr__(),
    #         "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
    #     )


