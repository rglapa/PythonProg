# odd-even / Brick sort
from re import I


def oddEvenSort(arr: list, n:int) -> None:
    # Initially array is unsorted
    is_sorted = 0
    while is_sorted == 0:
        is_sorted = 1
        temp = 0
        for i in range(1, n-1,2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = 0
        
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = 0

arr = [34, 2, 10, -9]
n = len(arr)

oddEvenSort(arr, n)
for i in range(0, n):
    print(arr[i], end=' ')