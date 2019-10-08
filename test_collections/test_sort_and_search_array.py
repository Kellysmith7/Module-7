import unittest
from fun_with_collections.sort_and_search_array import search_array
from fun_with_collections.sort_and_search_array import sort_array


class MyTestCase(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search_array(['cat', 'dog', 'mouse', 'fish'], 'cat'),  0)

    def test_sort(self):
        self.assertEqual(sort_array([2, 3, 1, 6, 5]), ([1, 2, 3, 5, 6]))


if __name__ == '__main__':
    unittest.main()
