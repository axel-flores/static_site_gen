from textnode import TextNode

def main():
    node = TextNode("Hello, World!", "text", "http://example.com")
    print(f"TextNode({node.text}, {node.text_type}, {node.url})")

main()