def counting(arr: list, exp1: int) -> None:
    n: int = len(arr)

    # The output array elements that will have sorted array
    output: list = [0] * n
    count: list = [0] * 10

    # Store count of occurances in count[]
    for i in range(0,n):
        index = arr[i]/exp1
        count[int((index)%10)] += 1
    
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]
    
    # Build the output array
    i = n-1
    while i>=0:
        index = arr[i]/exp1
        output[count[int(index%10)] -1] = arr[i]
        count[int(index%10)] -= 1
        i -= 1
    
    # Copy the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

def radixSort(arr: list) -> None:
    max1 = max(arr)

    exp = 1
    while max1/exp > 0:
        counting(arr, exp)
        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2,66]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
