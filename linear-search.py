#linear search in an array
#find the target element and return the index of the target element
def linear_search(nums,target):
  n = len(nums)
  for i in range(0,n):
    if nums[i] == target:
      return i
  return "no target element exist in the array"

nums = [21,4,3,5,1,65,2,44,23,12]
print(linear_search(nums,2))


