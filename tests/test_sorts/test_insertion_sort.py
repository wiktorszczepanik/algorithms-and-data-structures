import unittest
from algorithms.sorts.insertion_sort import insertion_sort
from constants.constants import EMPTY_LIST


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.basic_int_array = [3, -1, 4, 0, -5, 2, -4, 1, -3, -2, 5]
        self.basic_float_array = [2.2, -4.4, 0.0, 1.1, -5.5, 3.3, -1.1, -2.2, 4.4, -3.3, 5.5]
        self.single_element_array = [0]
        self.empty_array = []

        self.result_for_basic_int_array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.result_for_basic_float_array = [-5.5, -4.4, -3.3, -2.2, -1.1, 0.0, 1.1, 2.2, 3.3, 4.4, 5.5]
        self.result_for_single_element_array = [0]
        self.result_for_empty_array = []

    def test_basic_int_array_insertion_sort(self):
        array = self.basic_int_array
        length = len(array)
        result = self.result_for_basic_int_array
        self.assertEqual(insertion_sort(array, length), result)

    def test_basic_float_array_insertion_sort(self):
        array = self.basic_float_array
        length = len(array)
        result = self.result_for_basic_float_array
        self.assertEqual(insertion_sort(array, length), result)

    def test_single_array_insertion_sort(self):
        array = self.single_element_array
        length = len(array)
        result = self.result_for_single_element_array
        self.assertEqual(insertion_sort(array, length), result)

    def test_empty_array_insertion_sort(self):
        array = self.empty_array
        length = len(array)
        result = self.result_for_empty_array
        self.assertEqual(insertion_sort(array, length), EMPTY_LIST)


if __name__ == '__main__':
    unittest.main()
