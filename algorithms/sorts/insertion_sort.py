from typing import List, Union


def insertion_sort(array: List[Union[int, float]],
    length: int = None) -> List:
    if length is None:
        length = len(array)

    for next in range(length):
        curr = next
        temp = array[next]
        while curr > 0 and temp < array[curr - 1]:
            array[curr] = array[curr - 1]
            curr -= 1

        array[curr] = temp

    return array


# array = [6, 1, 5, 9, 2, 4, 7, 3, 8, 10]
# print(insertion_sort(array))
