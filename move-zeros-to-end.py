#move all zeros to end while maintaning the order
#brute force approach
def moveZeros(nums):
  n = len(nums)
  temp = []
  for i in range(0,n):
    if nums[i]!=0:
      temp.append(nums[i])
  
  nz = len(temp)
  for i in range(0,nz):
    nums[i] = temp[i]
  
  for i in range(nz,n):
    nums[i] = 0
  
  return nums

nums = [2,45,0,21,0,0,12,45,34,9]
print(moveZeros(nums))

#optimal solution
def move_zeros(nums):
  n = len(nums)
  if n == 1:
    return nums
  i = 0
  while i < n:
    if nums[i] == 0:
      break
    i += 1
  if i == n:
    return nums
  j = i+1
  while j<n:
    if nums[j] != 0:
      nums[i] , nums[j] = nums[j] , nums[i]
      i+=1
    j += 1
  return nums
  
nums1 = [23, 0, 0, 12, 3, 12,0,33]
print(move_zeros(nums1))


