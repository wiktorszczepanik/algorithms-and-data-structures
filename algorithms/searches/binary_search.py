from typing import List, Union
from constants.constants import NOT_FOUND


def binary_search(array: List[Union[int, float]],
    key: Union[int, float], length: int = None) -> int:

    if length is None:
        length = len(array)
    l: int = 0
    r: int = length - 1

    while l <= r:
        m: int = int((l + r) / 2)
        if array[m] == key:
            return m
        if array[m] > key:
            r = m - 1
        else:
            l = m + 1

    return NOT_FOUND


# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# key = 3
# length = len(array)
# print(binary_search(array, key)) # 2
