import unittest

from extract_title import extract_title

class TestTextNode(unittest.TestCase):
    def test_title(self):
        node = extract_title('# Hello')
        self.assertEqual(node, 'Hello')

if __name__ == "__main__":
    unittest.main()