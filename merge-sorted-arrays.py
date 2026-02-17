#merge two sorted arrays where no duplicate element allowed
def merge_arrays(num1,num2):
  n = len(num1) 
  z = len(num2)
  result = []
  i = 0
  j = 0
  while i < n and j < z:
    if num1[i] <= num2[j]:
      if len(result)== 0 or result[-1] != num1[i]:
        result.append(num1[i])
      i += 1
    else:
      if len(result)== 0 or result[-1] != num2[j]:
        result.append(num2[j])
      j += 1
  
  while i <n:
    if len(result)== 0 or result[-1] != num1[i]:
        result.append(num1[i])
    i += 1

  while j < z:
    if len(result)== 0 or result[-1] != num2[j]:
        result.append(num2[j])
    j += 1

  return result

num1 = [1,1,1,2,4,6,7]
num2 = [1,2,3,6,7,8,9,10]
print(merge_arrays(num1, num2))





