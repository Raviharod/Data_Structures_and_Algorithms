#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#0 <= a, b, c, d < n
#a, b, c, and d are distinct.
#nums[a] + nums[b] + nums[c] + nums[d] == target
#You may return the answer in any order.

#Brute force solution
def fourSum(nums):
  n = len(nums)
  mySet = set()
  for i in range(0,n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        for l in range(k+1,n):
          total_sum = nums[i]+nums[j]+nums[k]+nums[l]
          if total_sum == 0:
            temp = [nums[i],nums[j],nums[k],nums[l]]
            temp.sort()
            mySet.add(tuple(temp))
  return [list(ans) for ans in mySet]


nums1 = [1,0,-1,0,-2,2]
print(fourSum(nums1))

#Better Solution
def four__Sum(nums):
  n = len(nums)
  my_set = set()
  for i in range(0,n):
    for j in range(i+1,n):
      hash_set = set()
      for k in range(j+1,n):
        fourth = 0 - (nums[i] + nums[j] + nums[k])
        if fourth in hash_set:
          temp = [nums[i], nums[j], nums[k], fourth]
          temp.sort()
          my_set.add(tuple(temp))
        hash_set.add(nums[k])
  return [list(ans) for ans in my_set]

nums2 = [1,0,-1,0,-2,2]
print(four__Sum(nums2))

#optimal solution
def four_sum(nums):
  n = len(nums)
  result = []
  nums.sort()
  for i in range(0,n):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    for j in range(i+1,n):
      if j > i+1 and nums[j] == nums[j-1]:
        continue
      k = j+1
      l = n-1
      while k<l:
        total_sum = nums[i]+nums[j]+nums[k]+nums[l]
        if total_sum < 0:
          k += 1
        elif total_sum> 0:
          l -= 1
        else:
          result.append([nums[i],nums[j],nums[k],nums[l]])
          k += 1
          l -= 1

          while k < l and nums[k] == nums[k-1]:
            k += 1
          while k < l and nums[l] == nums[l+1]:
            l -= 1
  return result

nums = [1,0,-1,0,-2,2]
print(four_sum(nums))