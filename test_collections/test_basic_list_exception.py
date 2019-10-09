import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as topic1


class TestList(unittest.TestCase):
    def test_below_range(self):
        with self.assertRaises(ValueError):
            topic1.get_input()

    def test_above_range(self):
        with self.assertRaises(ValueError):
            topic1.get_input()



if __name__ == '__main__':
    unittest.main()
