from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        if self.children == None:
            raise ValueError("No children")
        
        output = ""

        if isinstance(self, ParentNode):
            att = self.props_to_html()
            output += f"<{self.tag}{att[:-1]}>\n"
            for child in self.children:
                output += child.to_html() + "\n"
            output += f"</{self.tag}>"
       
        return output
        

        
          
