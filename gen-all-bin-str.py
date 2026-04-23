'''generate all binary string such that there is no adjacent set bit'''


#Good Solution
def convert(num):
  bin = f"{num:b}"
  if not((num&(num>>1))>0):
    return bin

arr = [] 
def gen_bin(num,ind):
  if ind > num:
    return
  bin_ver = convert(ind)
  if bin_ver is not None:
    arr.append(bin_ver)
  gen_bin(num,ind+1)
  return arr

print(gen_bin(10,1))

#optimal solution
class Solution:
  def solve(self, index, flag, numbers, result):
    if index >= len(numbers):
      result.append("".join(numbers))
      return
    numbers[index] = "0"
    self.solve(index+1, True, numbers, result)
    if flag == True:
      numbers[index] = "1"
      self.solve(index+1, False, numbers, result)
      numbers[index] = "0"

  def generateBinStrings(self, n):
    numbers = ["0"]*n
    result = []
    self.solve(0,True,numbers,result)
    return result
  
binStr = Solution()
res = binStr.generateBinStrings(3)
print(res)


