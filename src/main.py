from parentnode import *
from leafnode import *
from textnode import *

def main():
    node = TextNode("Sample text", "bold")

    node2 = text_node_to_html_node(node)

    print(node2)

    test_str = "LeafNode(b, Sample text, )"

main()