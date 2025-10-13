from enum import Enum

class TextType(Enum):
    TEXT = "text",
    BOLD = "bold",
    ITALIC = "italic",
    UNDERLINE = "underline",
    STRIKETHROUGH = "strikethrough",
    LINK = "link",
    IMAGE = "image",
    CODE = "code",
    QUOTE = "quote",
    LIST = "list",
    LIST_ITEM = "list_item"

class TextNode:
    def __init__(self, text, text_type=TextType.TEXT, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def _repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
