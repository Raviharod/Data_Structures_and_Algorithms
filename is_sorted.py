# checking if array is sorted
def is_sorted(nums):
    n = len(nums)
    for i in range(0,n-1):
        if nums[i+1] < nums[i]:
            return False
    return True
nums = [1,3,7,7,7,8,9]
print(is_sorted(nums))