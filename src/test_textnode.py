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

    def test_split_func(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        str = repr(new_nodes)
        test_str = "[TextNode(This is text with a , text), TextNode(code block, code), TextNode( word, text)]"
        self.assertEqual(str, test_str)
    def test_split_func2(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("This is text with a `code block word", "text")
            new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(str(context.exception), "Invalid markdown syntax. No closing delimiter found.")
    def test_split_func3(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("This is text with a `code block` word", "text")
            new_nodes = split_nodes_delimiter([node], "$", "code")
        self.assertEqual(str(context.exception), "Invalid markdown syntax. Please provide the appropriate delimiter.")

    def test_extract_markdown_images_func(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        str = repr(extract_markdown_images(text))
        test_str = """[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]"""
        self.assertEqual(test_str, str)

    def test_extract_markdown_links_func(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        str = repr(extract_markdown_links(text))
        test_str = """[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]"""
        self.assertEqual(test_str, str)

if __name__ == "__main__":
    unittest.main()