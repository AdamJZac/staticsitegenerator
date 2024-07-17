from parentnode import ParentNode
from leafnode import LeafNode

def main():
    lnode1 = LeafNode("h3", "Third header")
    lnode2 = LeafNode("p", "Some paragraph text.")
    lnode3 = LeafNode("b", "Some bold text.")
    lnode4 = LeafNode("h4", "Fourth header")

    node = ParentNode("h1", [lnode2, lnode3])
    node2 = ParentNode("h2", [lnode1, lnode4, lnode2])
    node3 = ParentNode("body", [node, node2])

    print(node3.to_html())

main()