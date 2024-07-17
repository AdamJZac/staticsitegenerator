import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def testeq(self):
        lnode1 = LeafNode("h1", "Main header")
        lnode2 = LeafNode("p", "Some paragraph text.")
        lnode3 = LeafNode("b", "Some bold text.")
        
        node = ParentNode("body", [lnode1, lnode2, lnode3])
        str = "".join(node.to_html().split("\n"))
        test_str = "<body><h1>Main header</h1><p>Some paragraph text.</p><b>Some bold text.</b></body>"
        self.assertEqual(str, test_str)
    def testeq2(self):
        test_str = "<body><h1><p>Some paragraph text.</p><b>Some bold text.</b></h1><h2><h3>Third header</h3><h4>Fourth header</h4><p>Some paragraph text.</p></h2></body>"

        lnode1 = LeafNode("h3", "Third header")
        lnode2 = LeafNode("p", "Some paragraph text.")
        lnode3 = LeafNode("b", "Some bold text.")
        lnode4 = LeafNode("h4", "Fourth header")

        node = ParentNode("h1", [lnode2, lnode3])
        node2 = ParentNode("h2", [lnode1, lnode4, lnode2])
        node3 = ParentNode("body", [node, node2])

        str = "".join(node3.to_html().split("\n"))

        self.assertEqual(str, test_str)

if __name__ == "__main__":
    unittest.main()
