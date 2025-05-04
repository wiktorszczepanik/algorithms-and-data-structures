from typing import List


def quick_sort(array: List[int], left: int, right: int) -> List:
    if left < right:
        k = partition(array, left, right)
        quick_sort(array, left, k - 1)
        quick_sort(array, k + 1, right)
    return array


def partition(array: List[int], left: int, right: int) -> int:
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)
    swap(array, i + 1, right)
    return i + 1


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# array = [6, 1, 5, 9, 2, 4, 7, 3, 8, 10]
# print(quick_sort(array, 0, len(array) - 1))
