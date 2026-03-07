'''Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.'''

#Brute force solution
def findMin(nums):
  min = float("+infinity")
  for num in nums:
    if num<min:
      min = num
    else:
      continue
  return min
nums = [4,5,6,7,0,1,2]
print(findMin(nums))

#Optimal Solution
def find_min(nums):
  n = len(nums)
  min = float("+infinity")
  low = 0
  high = n-1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] <= nums[high]:
      if nums[mid] < min:
        min = nums[mid]
      high = mid-1
    else:
      if nums[low] < min:
        min = nums[low]
      low = mid+1
  return min

nums1 = [4,5,6,7,0,1,2]
print(find_min(nums1))