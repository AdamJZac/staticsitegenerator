from enum import Enum
from leafnode import LeafNode
import re

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
            output.append(node)
        else:
            lst = node.text.split(delimiter)
            type_order = []
            new_nodes = []

            if delimiter == node.text[0] or delimiter == node.text[0:2]:
                type_order.append(text_type+"_start")
            else:
                type_order.append("text")

            for i in range(1, len(node.text)-1):
                if delimiter == node.text[i] or delimiter == node.text[i:i+2]:
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

            print(lst)
            print(type_order)
            for j in range(0, len(lst)):
                new_node = TextNode(lst[j], type_order[j])
                print(new_node)
                new_nodes.append(new_node)
            
            output.extend(new_nodes)
                    
    return output      
    
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    output = []
    
    for node in old_nodes:
        images = extract_markdown_images(node.text)

        if not images:
            output.append(node)
            continue

        remaining_str = node.text
        for i in range(0, len(images)):
            image_alt, image_link = images[i]

            split_str = remaining_str.split(f"![{image_alt}]({image_link})", 1)
            output.append(TextNode(split_str[0], "text"))
            output.append(TextNode(image_alt, "image", image_link))
            remaining_str = split_str[1]
        if remaining_str:
            output.append(TextNode(remaining_str, "text"))

    if not output:
        return old_nodes
    else:
        return output

def split_nodes_links(old_nodes):
    output = []
    
    for node in old_nodes:
        links = extract_markdown_links(node.text)

        if not links:
            output.append(node)
            continue

        remaining_str = node.text
        for i in range(0, len(links)):
            link_text, link_url = links[i]

            split_str = remaining_str.split(f"[{link_text}]({link_url})", 1)
            output.append(TextNode(split_str[0], "text"))
            output.append(TextNode(link_text, "link", link_url))
            remaining_str = split_str[1]
        
        if remaining_str:
            output.append(TextNode(remaining_str, "text"))

    if not output:
        return old_nodes
    else:
        return output

def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes
