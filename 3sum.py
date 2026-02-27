#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#brute force solution
def threeSum(nums):
  n= len(nums)
  my_set = set()
  for i in range(0,n):
    for j in range(0,n):
      for k in range(0,n):
        if nums[i] + nums[j] +nums[k] == 0:
          temp = [nums[i], nums[j], nums[k]]
          temp.sort()
          my_set.add(tuple(temp))
  return [list(ans) for ans in my_set]


nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))

#better solution
def three_sum(nums):
  n = len(nums)
  result = set()
  for i in range(0,n):
    my_set = set()
    for j in range(i+1):
      third = -(nums[i] + nums[j])
      if third in my_set:
        temp = [nums[i], nums[j], third]
        temp.sort()
        result.add(tuple(temp))
      my_set.add(nums[j])
  return [list(ans) for ans in result]

nums1 = [-1,0,1,2,-1,-4]
# print(three_sum(nums1))

#optimal solution
def three_sum_opt(nums):
  n = len(nums)
  result = []
  nums.sort()
  for i in range(0,n):
    if i != 0 and nums[i] == nums[i-1]:
      continue

    j = i+1
    k = n-1
    while j < k:
      total_sum = nums[i]+nums[j]+nums[k]
      if total_sum < 0:
        j += 1
      elif total_sum > 0:
        k -= 1
      else:
        result.append([nums[i], nums[j], nums[k]])
        j += 1
        k -= 1

        while j < k and nums[j] == nums[j-1]:
          j += 1
        while j < k and nums[k] == nums[k+1]:
          k -= 1
  return result      

nums2 = [-1,0,1,2,-1,-4]
print(three_sum_opt(nums2))