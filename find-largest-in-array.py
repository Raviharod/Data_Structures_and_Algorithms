#first approach
def largestEle(nums):
    n = len(nums)
    largest = nums[0]
    for i in range(0,n):
        largest = max(largest, nums[i])
    return largest

nums = [-32, 22, 55, -64, 99, -123]
print(largestEle(nums))

#second approach
def largestElem(nums):
    n = len(nums)
    largest = float("-inf")
    for i in range(0,n):
        largest = max(largest, nums[i])
    return largest

nums = [-32, 22, 55, -64, 99, -123]
print(largestElem(nums))