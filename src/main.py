from parentnode import *
from leafnode import *
from textnode import *

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(text)
    print(f"Actual output: {new_nodes}")
    # [
    #     TextNode("This is text with a link ", text_type_text),
    #     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
    #     TextNode(" and ", text_type_text),
    #     TextNode(
    #         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]

main()