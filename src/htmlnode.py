class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        return " ".join(f"{key}=\"{value}\"" for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Value cannot be None or empty")
        if not self.tag:
            return self.value
        else:
            if self.props:
                props = " " + self.props_to_html()
            else:
                props = ""
            html_tag = f"<{self.tag}{props}>{self.value}</{self.tag}>"
            return html_tag
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannnot be None or empty")
        
        if not self.children:
            raise ValueError("Children cannot be None or empty")
        else:
            children_html = "".join(child.to_html() for child in self.children)
            return f"<{self.tag}>{children_html}</{self.tag}>"

        
        


    


