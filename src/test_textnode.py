import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
    def test_eq3(self):
        node = TextNode("This is a text node", "bold", "http://test")
        node2 = TextNode("This is a text node", "bold", "http://test")
        self.assertEqual(node, node2)
    def test_eq4(self):
        node = TextNode("Sample text", "bold")
        node2 = text_node_to_html_node(node)
        str = repr(node2)
        test_str = "LeafNode(b, Sample text, )"
        self.assertEqual(test_str, str)

    def test_uneq(self):
        node = TextNode("This is a text node", "italic", "http://test")
        node2 = TextNode("This is a text node", "bold", "http://test")
        self.assertNotEqual(node, node2)
    def test_uneq2(self):
        node = TextNode("This is a text node", "bold", "http://test")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)
    def test_uneq3(self):
        node = TextNode("This is a text node", "bold", "")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)
    def test_uneq4(self):
        node = TextNode("Text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()