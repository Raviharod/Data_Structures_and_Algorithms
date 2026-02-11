#bubble sort 
def bubble_sort(nums):
    n = len(nums)
    is_swap = False
    for i in range(0,n):
        for j in range(0, n-1):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if not is_swap:
            return nums

    return nums

nums = [5, 7, 2, 9, 1, 6, 3]
print(bubble_sort(nums))