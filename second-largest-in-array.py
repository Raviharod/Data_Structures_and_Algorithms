#brute force approach
def second_largest(nums):
    nums.sort()
    return nums[-2]

nums = [13,56,-25,88, 45,12,45, 95]
print(second_largest(nums))

#better approach
def sec_larg(nums):
    n = len(nums)
    largest = float("-inf")
    sec_largest = float("-inf")
    for i in range(0,n):
        largest = max(largest, nums[i])
    for i in range(0,n):
        if nums[i] > sec_largest and nums[i] != largest:
            sec_largest = nums[i]
    return second_largest

print(sec_larg(nums))

#optimal solution
def second_larg(nums):
    n = len(nums)
    largest = float("-inf")
    sec_largest = float("-inf")
    for i in range(0,n):
        if nums[i] > largest:
            sec_largest = largest
            largest = nums[i]
        elif nums[i] > sec_largest and nums[i] != largest:
            sec_largest = nums[i]
    return sec_largest

print(second_larg(nums))