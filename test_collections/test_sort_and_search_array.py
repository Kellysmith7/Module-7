import unittest
from fun_with_collections import sort_and_search_array

class MyTestCase(unittest.TestCase):
    def test_search(self):
        f = [2, 3, 4, 9]
        value = 5
        expected_result = -1
        self.assertEqual(-1, sort_and_search_array.search_array([2, 3, 4, 9], 5))

    # def test_sort(self):
    #     c = arr.array('d', [1.2, 6.3, 5.4])
    #     expected_result = 'array('d', [1.2, 5.4, 6.3])'
    #     self.assertEqual(('d', [1.2, 6.3, 5.4]), sort_array('array('d', [1.2, 5.4, 6.3])'))


if __name__ == '__main__':
    unittest.main()
