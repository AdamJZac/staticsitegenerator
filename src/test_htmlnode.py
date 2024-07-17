import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Sample text")
        node2 = HTMLNode("p", "Sample text")
        self.assertEqual(node, node2)
    def test_eq2(self):
        node_ch1 = HTMLNode()
        node_ch2 = HTMLNode()
        node = HTMLNode("p", "Sample text", [node_ch1, node_ch2], {"href": "https://www.test.com"})
        node2 = HTMLNode("p", "Sample text", [node_ch1, node_ch2], {"href": "https://www.test.com"})
        self.assertEqual(node, node2)
    def test_eq3(self):
        node = HTMLNode("p", "Sample text", None, {"href": "https://www.test.com"})
        node2 = HTMLNode("p", "Sample text", None, {"href": "https://www.test.com"})
        self.assertEqual(node, node2)
    def test_eq4(self):
        node = HTMLNode("p", "Sample text", None, {"href": "https://www.test.com"})
        node2 = HTMLNode("p", "Sample text", None, {"href": "https://www.test.com"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_uneq(self):
        node = HTMLNode("p", "Sample")
        node2 = HTMLNode("p", "Sample text")
        self.assertNotEqual(node, node2)
    def test_uneq2(self):
        node = HTMLNode("p", "Sample text", None, {"href": ""})
        node2 = HTMLNode("p", "Sample text", None, {"href": "https://www.test.com"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())



if __name__ == "__main__":
    unittest.main()