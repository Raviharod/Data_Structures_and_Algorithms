def combination_sum(ind, total,subset, nums, target, result):
  if total == target:
    result.append(subset.copy())
    return
  elif total > target:
    return
  if ind >= len(nums):
    return
  sum = total + nums[ind]
  subset.append(nums[ind])
  combination_sum(ind, sum, subset,nums,target,result)
  sum = total
  subset.pop()
  combination_sum(ind+1, sum, subset,nums,target,result)
  return result

target = 7
nums = [2,3,6,7]
result = []
subset = []
print(combination_sum(0,0,subset,nums,target,result))