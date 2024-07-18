import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def testeq(self):
        node = LeafNode("p", "Some text")
        node2 = LeafNode("p", "Some text")
        self.assertEqual(node, node2)
    def testeq2(self):
        node = LeafNode("p", "Some text")
        node2 = LeafNode("p", "Some text")
        self.assertEqual(node.to_html(), node2.to_html())
    def testeq3(self):
        node = LeafNode(None, "Plain text")
        str = "Plain text"
        self.assertEqual(node.to_html(), str)
    def testerr(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode("p")
            print(node.to_html())
        self.assertEqual(str(context.exception), "No value.")

        
        self.assertRaises(ValueError)

    def testuneq(self):
        node = LeafNode("p", "Some text")
        node2 = LeafNode("a", "Some text")
        self.assertNotEqual(node, node2)
    def testuneq2(self):
        node = LeafNode("p", "Some text", {"href": "http://"})
        node2 = LeafNode(None, "Some text", None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()