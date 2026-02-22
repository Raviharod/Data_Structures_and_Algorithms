#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#brute force solution
def long_conse_seq(nums):
  n = len(nums)
  max_count = 0
  for i in range(0,n):
    num = nums[i]
    count = 1
    while num+1 in nums:
      count += 1
      num += 1
    max_count = max(count , max_count)
    count = 1
  return max_count

num1 = [1,99,101,98,2,5,3,100,1,1]
print(long_conse_seq(num1))

#better solution
def lon_conse_seq(nums):
  n = len(nums)
  size = 0
  current = 0
  last_smaller = float("-infinity")
  nums.sort()
  for i in range(0,n):
    if last_smaller+1 == nums[i]:
      last_smaller = nums[i]
      current += 1
    else:
      last_smaller = nums[i]
      current = 1
    size = max(current, size)
  return size

nums = [100,4,200,1,3,2]
print(lon_conse_seq(nums))

#optimal solution
def longest_cons_seq(nums):
  my_set = set()
  for num in nums:
    my_set.add(num)
  
  largest = 0
  for num in nums:
    if num-1 not in nums:
      count = 1
      x = num
      while x+1 in my_set:
        count += 1
        x += 1
      largest = max(largest, count)
      count = 1
  return largest

nums2 = [1,99,101,98,2,5,3,100,1,1]
print(longest_cons_seq(nums2))
