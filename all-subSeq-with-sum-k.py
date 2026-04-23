'''Count all the subsequences with sum eqal to k'''

def countSubSeq(nums,target):
  def subSeq(ind,total):
    if total == target:
      return 1
    elif total > target:
      return 0
    if ind >= len(nums):
      return 0
    
    sum = total + nums[ind]
    pick = subSeq(ind+1,sum)
    sum = total
    n_pick = subSeq(ind+1,sum)
    return pick + n_pick
  return subSeq(0,0)

print(countSubSeq([9,7,5,4,8,1],9))