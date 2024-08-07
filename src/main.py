from parentnode import *
from leafnode import *
from textnode import *
from htmlnode import *
from helper import *

def main():
    text2 = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

```code```

>quotes
>morequotes

1. ordered list
2. list this"""

    text = """>quotes
>quotes2"""
    nodes = markdown_to_html_node(text)
    print(nodes)

main()