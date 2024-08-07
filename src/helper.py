from parentnode import *
from leafnode import *
from textnode import *
from htmlnode import *

tags_dict = {"quote": "<blockquote>", "paragraph": "<p>", "heading": "<h>"}

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    length = len(blocks)-1

    for i in range(length, 0, -1):
        blocks[i].strip()
        if blocks[i] == '':
            del blocks[i]
    
    return blocks

def block_to_block_type(block):
    block_type = "paragraph"
    chunks = block.split("\n")

    if chunks[0][0] == "#":
        block_type = "heading"
    elif chunks[0][0:3] == "```" and chunks[-1][-3:] == "```":
        block_type = "code"


    quote = True
    uo_list = True
    o_list = True
    for i in range(0, len(chunks)):
        if chunks[i][0] != ">":
            quote = False
        if chunks[i][0] != "*" and chunks[i][0] != "-":
            uo_list = False
        if chunks[i][0:2] != f"{i+1}.":
            o_list = False


    if quote:
        block_type = "quote"
    if uo_list:
        block_type = "unordered_list"
    if o_list:
        block_type = "ordered_list"


    return block_type

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        type = block_to_block_type(block)
        text_nodes = text_to_textnodes(block)
        children = []

        for node in text_nodes:
            children.append(text_node_to_html_node(node))
        
        nodes.append(ParentNode(tags_dict[type], children,))
    
    return nodes
    