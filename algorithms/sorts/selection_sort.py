from typing import List, Union

def selection_sort(array: List[Union[int, float]],
    length: int = None) -> List:
    if length is None:
        length = len(array)

    i: int = 0
    while i < length:
        mini = index_of_min(array, i)
        swap(array, i, mini)
        i += 1

    return array

def index_of_min(array: List, index) -> int:
    min_value = array[index]
    min_index = index

    for i in range(index, len(array)):
        if array[i] < min_value:
            min_value = array[i]
            min_index = i

    return min_index

def swap(array: List, index_1, index_2) -> None:
    temp_1 = array[index_1]
    array[index_1] = array[index_2]
    array[index_2] = temp_1

# array = [6, 1, 5, 9, 2, 4, 7, 3, 8, 10]
# print(selection_sort(array))
