from parentnode import *
from leafnode import *
from textnode import *

def main():
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)","text")
    new_nodes = split_nodes_links([node])
    print(new_nodes)
    # [
    #     TextNode("This is text with a link ", text_type_text),
    #     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
    #     TextNode(" and ", text_type_text),
    #     TextNode(
    #         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]

main()