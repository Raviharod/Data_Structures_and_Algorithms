'''There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.'''

#Brute force approach
def searchInRotatedarr2(nums,target):
  for num in nums:
    if num == target:
      return True
  return False

nums1 = [10,11,11,12,12,13,13,13,1,2,3,4]
print(searchInRotatedarr2(nums1,13))

#Optimal Solution
def searchInRotated(nums,target):
  n = len(nums)
  low = 0  
  high = n-1
  while low<=high:
    mid = (low+high)//2
    if nums[mid] == target:
      return True
    if nums[low] == nums[mid] == nums[high]:
      low += 1
      high -= 1
      continue
    if nums[mid] <= nums[high]:
      if nums[mid] <= target <= nums[high]:
        low = mid+1
        while low<=high and nums[low] == nums[low-1]:
          low += 1 
      else:
        high = mid-1
        while low<=high and nums[high] == nums[high+1]:
          high -= 1
    else:
      if nums[low] <= target <= nums[mid]:
        high = mid-1
        while low<=high and nums[high] == nums[high+1]:
          high -= 1
      else:
        low = mid +1
        while low<=high and nums[low] == nums[low-1]:
          low += 1 
  return False
nums = [7,7,7,7,7,7,7,1,2,3,4,5,7,7]
print(searchInRotated(nums,5))