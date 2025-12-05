import re

def extract_markdown_images(text):
    split_text = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)',text)
    return split_text

def extract_markdown_links(text):
    split_text = re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)',text)
    return split_text