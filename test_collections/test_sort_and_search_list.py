import unittest
from fun_with_collections import sort_and_search_list


class MyTestCase(unittest.TestCase):
    def test_sort(self):
        self.assertEqual([1.5, 2.3, 6, 6.6, 8.5, 9, 10.2], sort_and_search_list.sort_list())

    def test_search(self):
        self.assertEqual(0, sort_and_search_list.search_list())


if __name__ == '__main__':
    unittest.main()
