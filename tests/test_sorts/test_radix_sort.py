import unittest
from algorithms.sorts.radix_sort import radix_sort
from constants.constants import EMPTY_LIST


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # Only natural numbers applicable

        self.basic_int_array = [8, 3, 4, 0, 2, 7, 1, 5, 6, 9]
        self.basic_int_with_duplicates = [8, 8, 3, 4, 0, 0, 2, 7, 7, 1, 5, 6, 9]
        self.single_element_array = [0]
        self.empty_array = []

        self.result_for_basic_int_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.result_for_basic_int_with_duplicates = [0, 0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9]
        self.result_for_single_element_array = [0]
        self.result_for_empty_array = []


    def test_basic_int_array_radix_sort(self):
        array = self.basic_int_array
        length = len(array)
        result = self.result_for_basic_int_array
        self.assertEqual(radix_sort(array), result)


    def test_basic_int_with_duplicates(self):
        array = self.basic_int_with_duplicates
        length = len(array)
        result = self.result_for_basic_int_with_duplicates
        self.assertEqual(radix_sort(array), result)


    def test_single_array_radix_sort(self):
        array = self.single_element_array
        length = len(array)
        result = self.result_for_single_element_array
        self.assertEqual(radix_sort(array), result)


    def test_empty_array_radix_sort(self):
        array = self.empty_array
        length = len(array)
        self.assertEqual(radix_sort(array), EMPTY_LIST)


if __name__ == '__main__':
    unittest.main()
