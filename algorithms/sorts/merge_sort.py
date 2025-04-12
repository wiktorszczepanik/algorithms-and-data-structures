from typing import List, Union

def merge_sort(array: List[Union[int, float]],
    length: int) -> List:
    if length <= 1:
        return array[0:length]
    m = int(length / 2)
    return merge(merge_sort(array[0:m], m), m,
                 merge_sort(array[m:length], length - m), length - m)

def merge(array1: List, len1: int, array2: List, len2: int) -> List:
    i = j = k = 0
    result = [0] * (len1 + len2)

    while i < len1 and j < len2:
        if array1[i] < array2[j]:
            result[k] = array1[i]
            k += 1
            i += 1
        else:
            result[k] = array2[j]
            k += 1
            j += 1

    while i < len1:
        result[k] = array1[i]
        k += 1
        i += 1

    while j < len2:
        result[k] = array2[j]
        k += 1
        j += 1

    return result

# array = [6, 1, 5, 9, 2, 4, 7, 3, 8, 10]
# length = len(array)
# print(merge_sort(array, length))
