import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='7')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), ['7', '7', '7'])

    @patch('fun_with_collections.basic_list.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            topic1.make_list()


if __name__ == '__main__':
    unittest.main()
