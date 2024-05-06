import unittest
from main import search

class TestSearchFunction(unittest.TestCase):
    def test_exact_match(self):
        # Test exact match
        result = search("Sweater")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Sweater")

    def test_fuzzy_match(self):
        # Test fuzzy match
        result = search("Sweater")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Sweater")

    def test_no_match(self):
        # Test no match
        result = search("xyz")
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()

