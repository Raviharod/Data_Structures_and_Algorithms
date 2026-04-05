'''Check if any subsequence with sum eaqual to given target exist or not and return True or False as ans or you can return first subseq following this condition'''

def genereate_subSeq(nums,target):
  result = []
  subSet = []
  def findSeq(ind,total,subSet):
    if total == target:
      result.append(subSet.copy())
      return True
    elif total > target:
      return False
    if ind >= len(nums):
      return False
    
    subSet.append(nums[ind])
    total = total + nums[ind]
    pick = findSeq(ind+1, total,subSet)
    if pick == True:
      return True
    e = subSet.pop()
    total = total - e
    notPick = findSeq(ind+1,total,subSet)
    return notPick
  return findSeq(0,0,subSet)
  
print(genereate_subSeq([9,5,7,4],9))