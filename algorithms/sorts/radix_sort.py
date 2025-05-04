from typing import List
from constants.constants import EMPTY_LIST


def radix_sort(array: List[int]) -> List:
    if len(array) == 0:
        return EMPTY_LIST
    max_value = max(array)
    exp = 1
    while max_value / exp >= 1:
        count_sort(array, exp)
        exp *= 10

    return array


def count_sort(array, expression):
    length = len(array)
    output = [0] * length
    count = [0] * 10

    for i in range(0, length):
        index = array[i] // expression
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = length - 1
    while i >= 0:
        index = array[i] // expression
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, length):
        array[i] = output[i]


# array = [6, 1, 5, 9, 2, 4, 7, 3, 8, 10]
# print(radix_sort(array))
