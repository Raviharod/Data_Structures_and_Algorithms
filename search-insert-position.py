'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.'''
#Brute force solution
def searchInsert(nums,target):
  n = len(nums)
  for i in range(0,n):
    if nums[i] == target:
      return i
    elif nums[i] > target and i <= n:
      return i
    elif target != nums[i] and i==n-1:
      return n

nums = [1,2,4,6,6,8,9]
print(searchInsert(nums,9))

#Optimal solution
def search_insert(nums,target):
  n = len(nums)
  low = 0
  high = n-1
  position = n
  while low<=high:
    mid = (low+high)//2
    if nums[mid] >= target:
      position = mid
      high = mid -1
    else:
      low = mid + 1
  return position

nums1 = [1,2,4,6,6,8,9]
print(search_insert(nums1, 10))