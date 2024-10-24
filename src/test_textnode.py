import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_defaultURL(self):
        node = TextNode("This is a test2 node", "italic")
        node2 = TextNode("This is a test2 node", "italic")
        self.assertEqual(node.url, node2.url)

    def test_notEqual(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_defaultURL(self):
        node = TextNode("This is a test2 node", "italic", "www.league.com")
        node2 = TextNode("This is a test2 node", "italic", "www.league.com")
        self.assertEqual(node.url, node2.url)

    def test_text_node_to_html_node(self):
        node = TextNode("This is a test2 node", TextType.LINK, "www.league.com")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")

    def test_text_node_to_html_node_2(self):
        text_node = TextNode("This is a test node", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
    
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a test node")
        self.assertIsNone(html_node.props)

if __name__ == "__main__":
    unittest.main()