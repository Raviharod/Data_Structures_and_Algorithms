#find max consecutive ones in array and return its count
def max_cons_ones(nums):
  n = len(nums)
  count = 0
  max_count = 0
  for i in range(0, n):
    if nums[i] == 1:
      count += 1
    else:
      max_count = max(count, max_count)
      count = 0
  return max(count, max_count)
    
nums = [2,1,1,5,6,3,1,1,1,8,1]
print(max_cons_ones(nums))
    
