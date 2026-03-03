#implementation of lower and upper bound
#lower bound 
def lowerbound(nums,target):
  n = len(nums)
  lb = n
  low = 0
  high = n-1
  while low<=high:
    mid = (low+high)//2
    if nums[mid]>= target:
      lb = mid
      high = mid-1
    else:
      low = mid+1
  return lb

nums = [1,1,3,3,3,4,5,6,6,7,7,7,8,8]
print(lowerbound(nums, 3))

#upper bound
def upperbound(nums,target):
  n = len(nums)
  ub = n
  low = 0
  high = n-1
  while low<=high:
    mid = (low+high)//2
    if nums[mid]> target:
      ub = mid
      high = mid-1
    else:
      low = mid+1
  return ub

nums1 = [1,1,3,3,3,4,5,6,6,7,7,7,8,8]
print(upperbound(nums1, 3))