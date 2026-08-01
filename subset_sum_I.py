'''find all the subset sums and return them in a list
example: 
nums = [5,9,3]
solution 
[5]-> [5]
[9]-> [9]
[3]→3
[5,9]->14
[9,3]→12
[5,3]→8
[5,9,3]->17
[]->0
'''

def subset_sum_I(ind, total,nums, result):
  if ind >= len(nums):
    result.append(total)
    return
  sum = total + nums[ind]
  subset_sum_I(ind+1, sum,nums,result)
  sum = total
  subset_sum_I(ind+1, sum,nums,result)
  return result

print(subset_sum_I(0,0,[5,9,3],[]))


