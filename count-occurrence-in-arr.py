'''count the occurrence of the element in sorted array'''
#Brute force solution
def count_occurrence(nums,target):
  n = len(nums)
  first = -1
  last = -1
  for i in range(0,n):
    if nums[i] == target:
      if first == -1:
        first = i
      last = i
  return last-first+1

nums = [1,2,3,3,3,3,3,4,4,6,7,7,8]
print(count_occurrence(nums,3)) 

#Optimal Solution
def countOccurrences(nums,target):
  n = len(nums)
  lb = -1
  ub = n
  low1 = 0
  high1 = n-1
  
  while low1<=high1:
    mid = (low1+high1)//2
    if nums[mid] >= target:
      lb = mid
      high1 = mid-1
    else:
      low1 = mid+1

  low2 = 0
  high2 = n-1
  while low2<=high2:
    mid = (low2+high2)//2
    if nums[mid] > target:
      ub = mid
      high2 = mid-1
    else:
      low2 = mid+1
   
  return ub-lb

nums1 = [1,2,3,3,3,3,3,4,4,6,7,7,8]
print(countOccurrences(nums1,3))