import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode("<h1>", "", [], {})
        node2 = HtmlNode("<h1>", "", [], {})
        self.assertEqual(node.tag, node2.tag)

    def test_repr(self):
        node = HtmlNode("<h1>", "John", ["table", "section"], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual( f"HtmlNode(<h1>, John, {node.children}, {node.props})", repr(node))

    def test_props(self):
        node = HtmlNode("<h1>", "", [], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")

    def test_eqLeafNode(self):
        node = LeafNode("h1", "Hello World", {})
        node2 = LeafNode("h1", "Hello World", {})
        self.assertEqual(node.value, node2.value)

    def test_valueError(self):
        node = LeafNode("h1", "", {})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "There must be a value in leaf node")

    def test_htmlConvert(self):
        node = LeafNode("h1", "Hello World", {})
        self.assertEqual("<h1>Hello World</h1>", node.to_html())

    def test_htmlConvertWithProps(self):
        node = LeafNode("h1", "Hello World", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("<h1 href=\"https://www.google.com\" target=\"_blank\">Hello World</h1>", node.to_html())

    def test_eqParentNode(self):
        node = ParentNode("h1", [LeafNode("b", "Bold text"),
                                 LeafNode(None, "Normal text")], {})
        node2 = ParentNode("h1", [LeafNode("b", "Bold text"),
                                  LeafNode(None, "Normal text")], {})
        self.assertEqual(node.tag, node2.tag)

    def test_valueErrorParent(self):
        node = ParentNode("h1", None, {})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "There must be a child node in parent node")

    def test_toHtmlParentNode(self):
        node = ParentNode("p",  [LeafNode("b", "Bold text"), 
                                 LeafNode(None, "Normal text"), 
                                 LeafNode("i", "italic text"),
                                 LeafNode(None, "Normal text"),], {})
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()