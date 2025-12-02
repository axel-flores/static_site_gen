from enum import Enum
from textnode import *

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
