from enum import Enum
from leafnode import LeafNode

class TextNode:
    types = ["text", "bold", "italic", "code", "link", "image"]

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return ((self.text == other.text) and 
                (self.text_type == other.text_type) and
                (self.url == other.url))
    
    def __repr__(self):
        if self.url:
            return f"TextNode({self.text}, {self.text_type}, {self.url})"
        else:
            return f"TextNode({self.text}, {self.text_type})"

def text_node_to_html_node(text_node):  
    if text_node.text_type not in TextNode.types:
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
            
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    delimiters = {"code": "`", "bold": "**", "italic": "*"}

    if delimiter != delimiters[text_type]:
        raise ValueError("Invalid markdown syntax. Please provide the appropriate delimiter.")

    for node in old_nodes:
        if node.text_type != "text":
            output.extend(node)
        else:
            lst = node.text.split(delimiter)
            type_order = []
            new_nodes = []

            if delimiter == node.text[0] or delimiter == node.text[0:1]:
                type_order.append(text_type+"_start")
            else:
                type_order.append("text")

            for i in range(1, len(node.text)-1):
                if delimiter == node.text[i] or delimiter == node.text[i:i+1]:
                    if type_order[-1] != text_type+"_start":
                        type_order.append(text_type+"_start")
                    elif type_order[-1] == text_type+"_start":
                        type_order[-1] = text_type
                else:
                    if type_order[-1] != "text" and ("_start" not in type_order[-1]):
                        type_order.append("text")
            
            if delimiter == node.text[len(node.text)-1]:
                    if type_order[-1] != text_type+"_start":
                        type_order.append(text_type+"_start")
                    elif type_order[-1] == text_type+"_start":
                        type_order[-1] = text_type
            else:
                if type_order[-1] != "text" and ("_start" not in type_order[-1]):
                    type_order.append("text")

            if "_start" in type_order[-1]:
                raise ValueError("Invalid markdown syntax. No closing delimiter found.")

            for j in range(0, len(lst)):
                new_nodes.append(TextNode(lst[j], type_order[j]))
            
            output.extend(new_nodes)
                    
    return output      
    