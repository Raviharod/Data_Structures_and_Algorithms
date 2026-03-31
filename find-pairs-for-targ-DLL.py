'''find the pairs for the given sum in sorted doubly linked list with unique elements'''

import doublyLinkedList as DLL;
linkedList = DLL.DoublyLinkedList()

linkedList.append(1)
linkedList.append(2)
linkedList.append(4)
linkedList.append(5)
linkedList.append(6)
linkedList.append(8)
linkedList.append(9)

#Brute force solution
def findPairs(linkedList, target):
  temp1 = linkedList.head
  result = []
  while temp1 is not None:
    temp2 = temp1.next
    while temp2 is not None:
      if temp1.value + temp2.value == target:
        result.append([temp1.value, temp2.value])
        break
      temp2 = temp2.next
    temp1 = temp1.next
  return result

print(findPairs(linkedList, 7))


#Better solution
def find_pairs(linkedList, target):
  my_set = set()
  result = []
  temp = linkedList.head
  while temp is not None:
    remaining = target - temp.value
    if remaining in my_set:
      result.append([remaining, temp.value])
    
    my_set.add(temp.value)
    temp = temp.next
  return result

print(find_pairs(linkedList, 7))


#optimal solution
def find_pairsDLL(linkedList, target):
  result = []
  left = linkedList.head
  right = linkedList.head
  while right is not None:
    right = right.next
  
  right = right.prev
  while left.value < right.value:
    sum = left.value + right.value
    if sum == target:
      result.append([left.value, right.value])
      left = left.next
      right = right.prev
    elif sum > target:
      right = right.prev
    else:
      left = left.next
  return result

print(find_pairsDLL(linkedList, 7))
