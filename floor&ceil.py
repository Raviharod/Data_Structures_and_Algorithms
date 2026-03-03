'''we have to return the array of floor and ceil elements as the same elemnts if found otherwise floor is the highest of elements less than target and ceil is the greatest of elements greater than target'''

#My first approach
def floorAndCeil(nums,target):
  n = len(nums)
  low = 0
  high = n-1
  position = n
  while low <= high:
    mid = (low+high)//2
    if nums[mid] >= target:
      position = mid
      high = mid - 1
    else:
      low = low+1
  if position < n and nums[position] == target:
    return [nums[position], nums[position]]
  elif target < nums[0]:
    return [-1, nums[0]]
  elif position == n and target > nums[-1]:
    return [nums[-1], -1]
  else:
    return [nums[position-1], nums[position+1]]

nums = [1,2,4,6,6,8,9]
print(floorAndCeil(nums,20))

#optimal Solution
def floor_and_ceil(nums,target):
  n = len(nums)
  floor = -1
  ceil = -1
  low = 0
  high = n-1
  while low<=high:
    mid = (low+high)//2
    if nums[mid] == target:
      return [nums[mid],nums[mid]]
    elif nums[mid] > target:
      ceil = nums[mid]
      high = mid-1
    else:
      floor = nums[mid]
      low = mid + 1
  return [floor, ceil]

nums1 = [1,2,4,6,6,8,9]
print(floor_and_ceil(nums1, 3))