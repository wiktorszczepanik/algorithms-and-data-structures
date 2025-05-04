import unittest
from algorithms.searches.jump_search import jump_search
from constants.constants import NOT_FOUND


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.odd_len_array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.even_len_array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
        self.basic_float_array = [-5.5, -4.4, -3.3, -2.2, -1.1, 0.0, 1.1, 2.2, 3.3, 4.4, 5.5]
        self.single_element_array = [0]
        self.empty_array = []


    def test_odd_len_array_jump_search_found(self):
        length, key = len(self.odd_len_array), 3
        self.assertEqual(jump_search(self.odd_len_array, key, length), 8)


    def test_odd_len_array_jump_search_found_last_element(self):
        length, key = len(self.odd_len_array), 5
        self.assertEqual(jump_search(self.odd_len_array, key, length), 10)


    def test_basic_even_array_jump_search_found(self):
        length, key = len(self.even_len_array), 2
        self.assertEqual(jump_search(self.even_len_array, key, length), 7)


    def test_basic_even_array_jump_search_found_last_element(self):
        length, key = len(self.even_len_array), 6
        self.assertEqual(jump_search(self.even_len_array, key, length), 11)


    def test_basic_float_array_jump_search_found(self):
        length, key = len(self.basic_float_array), 5.5
        self.assertEqual(jump_search(self.basic_float_array, key, length), 10)


    def test_odd_len_array_jump_search_not_found(self):
        length, key = len(self.odd_len_array), 10
        self.assertEqual(jump_search(self.odd_len_array, key, length), NOT_FOUND)


    def test_single_element_array_jump_search_found(self):
        length, key = len(self.single_element_array), 0
        self.assertEqual(jump_search(self.single_element_array, key, length), 0)


    def test_single_element_array_jump_search_not_found(self):
        length, key = len(self.single_element_array), 10
        self.assertEqual(jump_search(self.single_element_array, key, length), NOT_FOUND)


    def test_empty_array_jump_search_not_found(self):
        key = 1
        self.assertEqual(jump_search(self.empty_array, key), NOT_FOUND)



if __name__ == '__main__':
    unittest.main()
