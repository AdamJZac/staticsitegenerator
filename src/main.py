from parentnode import *
from leafnode import *
from textnode import *

def main():
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")

    print(new_nodes)

main()