from parentnode import *
from leafnode import *
from textnode import *
from htmlnode import *

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    length = len(blocks)-1

    for i in range(length, 0, -1):
        blocks[i].strip()
        if blocks[i] == '':
            del blocks[i]
    
    return blocks
