from textnode import *

def main():
    node = TextNode("This is a text node", "bold", None)
    node2 = TextNode("This is a text node", "bold", None)

    print(node == node2)

main()