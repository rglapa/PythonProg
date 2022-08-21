def search(arr: list, curr_index: int, key:int) -> int:
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)