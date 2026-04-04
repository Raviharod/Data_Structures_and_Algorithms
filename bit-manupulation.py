'''Starting the bit manupulation
converting decimal to binary
decimal = 9
binary = 1001
'''

def decToBin(num):
  result = ''
  while num > 0:
    rem = num%2
    result = f'{rem}'+ result
    num = num//2
  return result

print(decToBin(9))

'''convert binary to decimal'''
def binToDec(bin):
  decimal = 0
  power = 0
  size = len(bin)-1
  while size >= 0:
    decimal += int(bin[size])*2**power
    power += 1
    size -= 1
  return decimal

print(binToDec("1001"))

#Compliments
'''1's and 2's complement are methods to represent signed integers in binary, primarily used to simplify subtraction in computing. 1's complement flips all bits (0 to 1, 1 to 0), while 2's complement flips the bits and adds 1 to the result.
=>1's Complement
Method: Invert all bits (0 to 1, 1 to 0).
Example: For 5 (0101), 1's complement is (1010)
Usage: Used in one's complement arithmetic and sometimes in digital signal processing. 

=>2's Complement
Method: Find 1's complement and add 1 to the least significant bit (LSB).
Example: For 5 (0101): 1's complement (1010) + 1 = (1011)
Key Feature: Single representation of zero (0000 for 4 bits).
Usage: Standard in arithmetic logic units (ALUs) for addition and subtraction. 
'''

#swap two numbers using bit manupulation
def swapNums(a, b):
  temp = b
  b = (a^b)^b
  a = (a^temp)^a
  return f'a={a}, b={b}'

print(swapNums(10,12))

#check if ith bit is set bit or not
def checkSetBit(num,i):
  if (num & (1<<i)) == 1:#using left shift operator
    return True
  else:
    return False

print(checkSetBit(12,1))

def checkSet_bit(num,i):
  if (num>>i)&1 == 1:
    return True
  else:
    return False

print(checkSet_bit(12,2))

#set the ith bit
def setBit(num,i):
  return num|(1<<i)

print(setBit(12,1))

#clear the ith bit
def clearBit(num,i):
  return num&(~(1<<i))

print(clearBit(13,2))

#toggle the ith bit
def toggleBit(num,i):
  return num^(1<<i)

print(toggleBit(13,2))

#remove the rightmost set bit
def removeRightMostBit(num):
  return num&(num-1)
print(removeRightMostBit(40))

#check if the number is power of two
def checkPowerOfTwo(num):
  if num&(num-1) == 0:
    return True
  else:
    return False
  
print(checkPowerOfTwo(32));

#count the minimum number of flips to convert the number
def countFlips(start, goal):
  ans = start ^ goal
  count = 0
  for i in range(0,31):
    if ans&(1<<i) !=0:
      count += 1
  return count

print(countFlips(15,19))

#now we get the number occurs only once in arr using both brute force and bit manupulation
#Brute force approach
def findSingleEle(arr):
  hash_map = {}
  for num in arr:
    hash_map[num] =  hash_map.get(num,0)+1
  
  for key in hash_map:
    if hash_map[key] == 1:
      return "single element is=>", key
arr = [5,1,3,3,7,1,7,5,9]
print(findSingleEle(arr))


#optimal solution
def find_sing_ele(arr):
  ans = 0
  for num in arr:
    ans = ans^num
  return ans
arr1 = [5,1,3,3,7,1,7,5,9]
print(find_sing_ele(arr1))

#find all the subsets using bit manupulation
def findSubsets(arr):
  n = len(arr)
  total_subSets = 1<<n
  result = []
  for num in range(0,total_subSets):
    lst = []
    for i in range(0,n):
      if num&(1<<i) != 0:
        lst.append(arr[i])
    result.append(lst)
  return result
nums = [1,2,3]
print(findSubsets(nums))