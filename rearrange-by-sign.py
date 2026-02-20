#rearrange the elements by sign in alternate manner while preserving the order
#brute force approach
def rearrBySign(nums):
  n = len(nums)
  positive = []
  negative = []
  for i in range(0,n):
    if nums[i] >= 0:
      positive.append(nums[i])
    else:
      negative.append(nums[i])
  
  for i in range(0, len(positive)):
    nums[2*i] = positive[i]
    nums[(2*i)+1] = negative[i]

  print(nums)

nums1 = [5,10,-3,-1,-10,6]
rearrBySign(nums1)



#optimal solution
def rearr_by_sign(nums):
  n = len(nums)
  result = [0]*n
  pos_ind, neg_ind = 0,1
  for i in range(0,n):
    if nums[i] >= 0:
      result[pos_ind] = nums[i]
      pos_ind += 2
    else:
      result[neg_ind] = nums[i]
      neg_ind += 2
  return result
  

nums = [5,10,-3,-1,-10,6]
print(rearr_by_sign(nums))