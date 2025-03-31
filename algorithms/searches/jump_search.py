import math
from typing import List, Union

def jump_search(array: List[Union[int, float]], key: Union[int, float], length: int = None) -> int:
    if length is None:
        length = len(array)
    if length > 0 and key <= array[length - 1]:
        block_size: int = int(math.sqrt(length))
        step: int = block_size
        while step < length and key > array[step]:
            step = min(step + block_size, length)
        counter: int = 0
        for i in range(step - block_size, step + 1):
            if array[i] == key:
                return step - block_size + counter
            counter += 1
    return -1 # Not found

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# key = 3
# length = len(array)
# print(jump_search(array, key, length)) # 2
