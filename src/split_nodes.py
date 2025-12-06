from enum import Enum
from textnode import *
from split_markdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if(node.text.count(delimiter)) == 1:
            raise Exception("Delimiter found only once in text node, cannot split.")    
        parts = node.text.split(delimiter)
        for index, part in enumerate(parts):
            if part == "":
                continue
            if index % 2 == 1:
                new_nodes.append(TextNode(part, text_type=text_type))
            else:
                new_nodes.append(TextNode(part, text_type=TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        sections = []

        original_text = node.text

        sections = re.split(r'(!\[(?:[^\[\]]*)\]\((?:[^\(\)]*)\))', original_text)

        for sec in sections:
            if not sec:
                continue
            if not extract_markdown_images(sec):
                new_nodes.append(TextNode(sec, TextType.TEXT))
            else:
                for image_alt, image_link in extract_markdown_images(sec):
                    new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        sections = []

        original_text = node.text

        sections = re.split(r'(\[(?:[^\[\]]*)\]\((?:[^\(\)]*)\))', original_text)

        for sec in sections:
            if not sec:
                continue
            if not extract_markdown_links(sec):
                new_nodes.append(TextNode(sec, TextType.TEXT))
            else:
                for link_alt, image_link in extract_markdown_links(sec):
                    new_nodes.append(TextNode(link_alt, TextType.LINK, image_link))

    return new_nodes
#    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",

#     node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )

# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]