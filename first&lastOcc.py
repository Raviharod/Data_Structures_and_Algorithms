'''find the first and last occurrence indexes in sorted array for the target element and if target not exist return [-1,-1]'''

#Brute Force solution
def first_last_occu(nums,target):
  n = len(nums)
  first = -1
  last = -1
  for i in range(0,n):
    if i != 0 and nums[i] == target and nums[i] == nums[i-1]:
      last = i
      if i < n-1 and nums[i+1] != target:
        return [first,last]
    else:
      if nums[i] == target:
        first = i
    # print(i)
  return [first, last]

nums = [1,1,2,3,3,3,3,4,5,5]
print(first_last_occu(nums,5))

#Optimal Solution
class RangeFinder:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)

    def find_first(self, target):
        low, high = 0, self.n - 1
        first = -1
        while low <= high:
            mid = low + (high - low) // 2
            if self.nums[mid] >= target:
                if self.nums[mid] == target:
                    first = mid
                high = mid - 1
            else:
                low = mid + 1
        return first

    def find_last(self, target):
        low, high = 0, self.n - 1
        last = -1
        while low <= high:
            mid = low + (high - low) // 2
            if self.nums[mid] <= target:
                if self.nums[mid] == target:
                    last = mid
                low = mid + 1
            else:
                high = mid - 1
        return last

    def get_range(self, target):
        # Edge case: empty list
        if not self.nums:
            return [-1, -1]
            
        first = self.find_first(target)
        # If the first occurrence doesn't exist, the target isn't there at all
        if first == -1:
            return [-1, -1]
            
        last = self.find_last(target)
        return [first, last]


nums1 = [1, 1, 2, 3, 3, 3, 3, 4, 5, 5]
finder = RangeFinder(nums1)
print(finder.get_range(5))
