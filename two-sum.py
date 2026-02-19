#find the sum of two elements in an array that equals to target element and return their indexes
#brute force solution
def two_sum(nums,target):
  n = len(nums)
  for i in range(0, n-1):
    for j in range(i+1,n):
      if nums[i] + nums[j] == target:
        return [i,j]
  return "no indexes found"

nums = [0,3,-1,54,3,-33,44]
print(two_sum(nums,-1))

#optimal solution
def twoSum(nums, target):
  n = len(nums)
  hash_map = {}
  for i in range(0,n):
    remaining = target - nums[i]
    if remaining in hash_map:
      return [hash_map[remaining], i]
    hash_map[nums[i]] = i

nums1 = [32,45,1,23,65,-12]
print(two_sum(nums1,46))
