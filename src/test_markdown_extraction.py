import unittest

from split_markdown import *

class TestSplitMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "Here is an image ![alt text](image_url) in the text."
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "image_url")])

    def test_extract_markdown_links(self):
        text = "Here is a link [link text](link_url) in the text."
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link text", "link_url")])

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
