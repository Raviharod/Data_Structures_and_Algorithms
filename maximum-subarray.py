#Given an integer array nums, find the subarray with the largest sum, and return its sum.
#brute force solution
def maximum_subArr(nums):
  n = len(nums)
  total = 0
  max_sum = float("-infinity")
  for i in range(0,n-1):
    total = 0
    for j in range(i,n):
      # sliced = nums[i:j]
      # curr_sum = sum(sliced)
      total = total+nums[j]
      if total>max_sum:
        max_sum = total
    
  return max_sum

nums = [-2,4,-3,4,-1,5,1,-5,4]
print(maximum_subArr(nums))

#optimal solution
def max_subArr(nums):
  n = len(nums)
  total = 0
  max_sum = float("-infinity")
  for i in range(0,n):
    total = total + nums[i]
    max_sum = max(total, max_sum)
    if total < 0:
      total = 0
  return max_sum

nums1 = [-2,4,-3,4,-1,5,1,-5,4]
print(max_subArr(nums1))