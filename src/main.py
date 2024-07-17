from leafnode import LeafNode

def main():
    node = LeafNode("p", "This is a paragraph of text.")
    node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(node.to_html())
    print(node2.to_html())

main()