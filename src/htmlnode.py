class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value =  value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_list = []
        for key,value in self.props.items():
            props_list.append(f"{key}=\"{value}\"")
        return " ".join(props_list)
    
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("There must be a value in leaf node")
        if self.tag is None:
            return self.value
        if self.props:
            return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"       
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children is None:
            raise ValueError("There must be a child node in parent node")
        if self.tag is None:
            raise ValueError("There must be a tag in parent node")
        html_str = ""
        for child in self.children:
            html_str += child.to_html()

        if self.props:
            return f"<{self.tag} {super().props_to_html()}>{html_str}</{self.tag}>"        
        return f"<{self.tag}>{html_str}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    
    
