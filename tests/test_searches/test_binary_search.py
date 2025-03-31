import unittest
from algorithms.searches.binary_search import binary_search
from constants.constants import NOT_FOUND


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.basic_int_array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.basic_float_array = [-5.5, -4.4, -3.3, -2.2, -1.1, 0.0, 1.1, 2.2, 3.3, 4.4, 5.5]
        self.single_element_array = [0]
        self.empty_array = []

    def test_basic_int_array_binary_search_found(self):
        length, key = len(self.basic_int_array), 5
        self.assertEqual(binary_search(self.basic_int_array, key, length), 10)

    def test_basic_float_array_binary_search_found(self):
        length, key = len(self.basic_float_array), 5.5
        self.assertEqual(binary_search(self.basic_float_array, key, length), 10)

    def test_basic_array_binary_search_not_found(self):
        length, key = len(self.basic_int_array), 10
        self.assertEqual(binary_search(self.basic_int_array, key, length), NOT_FOUND)

    def test_single_element_array_binary_search_found(self):
        length, key = len(self.single_element_array), 0
        self.assertEqual(binary_search(self.single_element_array, key, length), 0)

    def test_single_element_array_binary_search_not_found(self):
        length, key = len(self.single_element_array), 10
        self.assertEqual(binary_search(self.single_element_array, key, length), NOT_FOUND)

    def test_empty_array_binary_search_not_found(self):
        length, key = len(self.empty_array), 1
        self.assertEqual(binary_search(self.empty_array, key, length), NOT_FOUND)


if __name__ == '__main__':
    unittest.main()
