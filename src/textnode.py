from enum import Enum
from leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return ((self.text == other.text) and 
                (self.text_type == other.text_type) and
                (self.url == other.url))
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    types = ["text", "bold", "italic", "code", "link", "image"]
    
    if text_node.text_type not in types:
        raise Exception(f"Invalid text type: {text_node.text_type}")
    else:
        match text_node.text_type:
            case "text":
                return LeafNode(None, text_node.text)
            case "bold":
                return LeafNode("b", text_node.text)
            case "italic":
                return LeafNode("i", text_node.text)
            case "code":
                return LeafNode("code", text_node.text)
            case "link":
                return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
            case "image":
                return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})