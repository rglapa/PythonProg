def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)

        # Else the element can only be present in the right subarray
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        # Element is not present in array
        return -1

# Test array
arr = [2,3,4,10,40]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")