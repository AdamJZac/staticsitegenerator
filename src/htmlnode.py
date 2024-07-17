class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        # A list of HTMLNode objects
        self.children = children
        # A dictionary of attributes and their values
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    
    def __eq__(self, other):
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = " "

        if self.props == None:
            return ""

        for key, value in self.props.items():
            output += f"""{key}="{value}" """

        return output