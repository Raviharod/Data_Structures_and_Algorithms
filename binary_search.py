#Binary search algorithm
"""
two approaches
1. Iterative solution
2. Recursive Solution
"""

#Iterative solution
def binary_search(nums, target):
  n = len(nums)
  low = 0
  high = n-1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low = mid+1
    else:
      high = mid-1
  return -1

nums = [1, 2, 5, 12, 34, 43, 53, 54, 76, 99, 123]
# print(binary_search(nums,1))


#Recursive solution
def bsc(nums,low,high,target):
  if low>high:
    return -1
  mid = (low+high)//2
  if nums[mid] == target:
    return mid
  elif nums[mid] < target:
    return bsc(nums,mid+1,high,target)
  else:
    return bsc(nums,low,mid-1,target)

def BinarySearch(nums,target):
  n = len(nums)
  low = 0 
  high = n-1
  print(bsc(nums,low,high,target))

nums1 = [1, 2, 5, 12, 34, 43, 53, 54, 76, 99, 123]
BinarySearch(nums1,12)
