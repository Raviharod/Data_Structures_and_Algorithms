'''Find all the sub-sequences in an array
example: [5,9,7]
output:[[5,9,7],[5,9],[5,7],[5],[9,7],[7],[9],[]]
'''


def findSubSeq(nums):
  result = []
  subSet = []
  def findSeq(ind,subSet):
    if ind >= len(nums):
      result.append(subSet.copy())
      return
    subSet.append(nums[ind])
    findSeq(ind+1,subSet)
    subSet.pop()
    findSeq(ind+1, subSet)
  findSeq(0,subSet)
  return result

print(findSubSeq([5,9,7]))


