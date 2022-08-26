def countSort(arr: list):
    # The output character array that will will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
    
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

arr = "geeksforgeeks"
ans = countSort(arr)
print('Sorted character array is %s' %(''.join(ans)))