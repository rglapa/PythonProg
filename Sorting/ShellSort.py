def shellSort(arr: list) -> None:
    # start with a big gap then reduce the gap
    n = len(arr)
    gap = (n/2)
    print(type(n))
    print(type(gap))
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]

            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            
            arr[j] = temp
        gap /= 2

arr = [12,34,54,2,3]
n = len(arr)

print("Array before sorting:")
for i in range(n):
    print(arr[i])

print('After sorting:')
shellSort(arr)
for i in range(n):
    print(arr[i])