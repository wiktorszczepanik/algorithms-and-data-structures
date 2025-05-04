from typing import List
from constants.constants import EMPTY_LIST


# Only natural numbers applicable
def count_sort(array: List[int], length: int = None) -> List:
    if length is None:
        length = len(array)

    if length == 0:
        return EMPTY_LIST

    max_value = max(array)
    max_value_pp = max_value + 1
    counts = [0] * max_value_pp
    results = [0] * length

    for i in range(0, length):
        counts[array[i]] += 1

    for i in range(1, max_value_pp):
        counts[i] += counts[i - 1]

    for i in range(length - 1, -1, -1):
        counts[array[i]] -= 1
        results[counts[array[i]]] = array[i]

    return results


# array = [6, 1, 5, 0, 9, 2, 4, 7, 3, 8, 10]
# print(count_sort(array))
