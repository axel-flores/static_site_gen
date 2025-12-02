import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestNodeSplit(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is a test. split here. this is after split.", TextType.TEXT)
        ]
        delimiter = " "
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This", TextType.TEXT),
                TextNode("is", TextType.BOLD),
                TextNode("a", TextType.TEXT),
                TextNode("test.", TextType.BOLD),
                TextNode("split", TextType.TEXT),
                TextNode("here.", TextType.BOLD),
                TextNode("this", TextType.TEXT),
                TextNode("is", TextType.BOLD),
                TextNode("after", TextType.TEXT),
                TextNode("split.", TextType.BOLD),
            ],
        )

    def test_split_nodes_delimiter_code(self):
        old_nodes = [
            TextNode("This is text with a `code block` word", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_italic(self):
        old_nodes = [
            TextNode("This is _italic_ text example", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text example", TextType.TEXT),
        ])
