#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
def rotateArray(nums,k): #brute force approach
    n = len(nums)
    rotations = k%n
    if rotations == 0:
        return nums
    for _ in range(0,rotations):
        last = nums.pop()
        nums.insert(0, last)
    return nums
nums = [1,2,3,4]
print(rotateArray(nums,2))


#optimal solution with slicing
def rotate_arr(nums,k):
    n = len(nums)
    rotations = k%n
    if rotations == 0:
        return nums
    nums[:] = nums[n-rotations:] + nums[0:n-rotations]
    return nums

nums1 = [2,4,6,8,9]
print(rotate_arr(nums1,3))

#optimal solution without slicing
def reverse(nums, left, right):
    while left<right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
def rot_Array(nums, k):
    n = len(nums)
    rotations = k%n
    reverse(nums, n-k, n-1)
    reverse(nums, 0, n-k-1)
    reverse(nums, 0, n-1)
    return nums

nums2 = [1,2,3,4,5,6,7,8]
print(rot_Array(nums2, 3))

