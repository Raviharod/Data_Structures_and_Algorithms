#remove duplicates from an array and count unique elements(brute force approach)
def removeDuplicates(nums):
    n = len(nums)
    dict = {}
    for i in range(0,n):
        dict[nums[i]] = 0
    j =0
    for key in dict:
        nums[j] = key
        j += 1
    return j

nums = [13,45,2,23,13,5,3,2,5,6,5,2,3]
print(removeDuplicates(nums))

#optimal solution
def remove_dupl(nums):
    n = len(nums)
    if n <= 1:
        return n
    
    i = 0 
    for j in range(1, n): 
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            
    return i + 1
nums1 = [1, 1, 2, 2, 3, 4, 4]
print(remove_dupl(nums1))
