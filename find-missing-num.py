#find missing number(index) from an array
#brute force solution
def find_missing(nums):
  n = len(nums)
  for i in range(0,n+1):
    if i not in nums:
      return i

nums = [4,0,1,2]
print(find_missing(nums))

#better solution
def find_miss(nums):
  n = len(nums)
  freq = {}
  for i in range(0,n+1):
    freq[i] = 0
  for i in nums:
    freq[i] = 1
  for key, value in freq.items():
    if value == 0:
      return key
  
nums1 = [4,1,3,2]
print(find_miss(nums1))

#optimal soltion
def find_miss_num(nums):
  n = len(nums)
  return (n*(n+1))/2 - sum(nums2)

nums2 = [4,1,3,2]
print(find_miss_num(nums2))


