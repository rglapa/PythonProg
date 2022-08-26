def stoogeSort(arr: list, l: int, h: int) -> None:
    if l >= h:
        return
    
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

        if h-l+1 > 2:
            t = int((h-l+1)/3)

            stoogeSort(arr, l, h-t)

            stoogeSort(arr, l+t, h)

            stoogeSort(arr, l, h-t)

arr: list = [2, 4, 5, 3, 1]
n = len(arr)

stoogeSort(arr, 0, n-1)
for i in range(0,n):
    print(arr[i], end=' ')