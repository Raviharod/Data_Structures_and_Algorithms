'''generate all the subsequences whose sum is eaqual to the target using recursion'''

#Brute force approach
def findSubSeq(nums,target):
  result = []
  subSet = []
  def findSeq(ind,subSet):
    if ind >= len(nums):
      if sum(subSet) == target:
        result.append(subSet.copy()) 
        return
      return
    subSet.append(nums[ind])
    findSeq(ind+1,subSet)
    subSet.pop()
    findSeq(ind+1, subSet)
  findSeq(0,subSet)
  return result

print(findSubSeq([5,9,7,4],9))


#Optimal solution
def genereate_subSeq(nums,target):
  result = []
  subSet = []
  def findSeq(ind,total,subSet):
    if total == target:
      result.append(subSet.copy())
      return
    elif total > target:
      return
    if ind >= len(nums):
      return 
    
    subSet.append(nums[ind])
    total = total + nums[ind]
    findSeq(ind+1, total,subSet)
    e = subSet.pop()
    total = total - e
    findSeq(ind+1,total,subSet)
  
  findSeq(0,0,subSet)
  return result

print(genereate_subSeq([9,5,7,4],9))