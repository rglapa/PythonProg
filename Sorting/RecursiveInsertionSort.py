
def insertionSortRecurive(arr: list, n: int):
    '''Recursive function to sort array''' 
    # base case
    if n <= 1:
        return
    
    # sort first n-1 elements
    insertionSortRecurive(arr, n-1)

    # Insert last element at its correct position in sorted array
    last = arr[n-1]
    j = n - 2

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j = j -1
    arr[j+1] = last

# sorting the array using insertionSort
if __name__ == "__main__":
    A = [-7, 11, 6, 0, -3, 5, 10, 2]
    n = len(A)
    insertionSortRecurive(A, n)
    print(A)