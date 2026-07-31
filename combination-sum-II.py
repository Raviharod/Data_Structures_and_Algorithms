'''Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''

#Brute Force Solution
def combination_sum_II(ind, total, subset,nums, target, result,myTuple):
  if total == target:
    subset.sort()
    tup = tuple(subset)
    if tup not in myTuple:
      myTuple.append(tup)
      result.append(subset.copy())
    return
  elif total > target:
    return
  if ind >= len(nums):
    return

  sum = total + nums[ind]
  subset.append(nums[ind])
  combination_sum_II(ind,sum,subset,nums,target,result,myTuple)
  sum = total
  subset.pop()
  combination_sum_II(ind+1,sum, subset,nums,target,result,myTuple)
  return result

target = 7
nums = [1,1,2,1,2]
result = []
subset = []
myTuple = []
# print(combination_sum_II(0,0,subset,nums,target,result,myTuple))

#Optimal solution
def comb_sum_II(ind,total,subset,nums,result):
  n = len(nums)
  if total == 0:
    result.append(subset.copy())
    return
  if total <0:
    return
  for i in range(ind,n):
    if i > ind and nums[i] == nums[i-1]:
      continue
    subset.append(nums[i])
    sum = total - nums[i]
    comb_sum_II(i+1,sum,subset,nums,result)
    subset.pop()
  return result

print(comb_sum_II(0,4,[],[1,1,1,2,3],[]))



