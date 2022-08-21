def partition(l, r, nums):
    '''Last element will be the pivot and the first element the pointer'''
    pivot, ptr = nums[r], l
    for i in range(l,r):
        if nums[i] <= pivot:
            # swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
        # finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l,r,nums)
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums)
    return nums

example = [4,5,1,2,3]
result = [1,2,3,4,5]
print(quicksort(0,len(example)-1, example))
