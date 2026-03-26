'''Reverse the doubly linked list and return it's head'''


import doublyLinkedList as DLL
linkedList = DLL.DoublyLinkedList()
linkedList.append(11)
linkedList.append(12)
linkedList.append(13)
linkedList.append(14)
linkedList.append(15)
linkedList.append(16)
linkedList.append(17)


#Brute force approach
def reverseDoublyLL(linkedList):
  if linkedList.head is None:
    return print(linkedList.head.value)
  arr = []
  curr = linkedList.head
  while curr is not None:
    arr.append(curr.value)
    curr = curr.next
  
  curr = linkedList.head
  while curr is not None:
    curr.value = arr.pop()
    curr = curr.next
  temp = linkedList.head
  while temp is not None:
    print(temp.value, end=" ")
    temp = temp.next
  
reverseDoublyLL(linkedList)


#Optimal Solution
def reverse_doubly_LL(linkedList):
  if linkedList.head is None:
    return print(linkedList.head.value)
  
  curr = linkedList.head
  prev = None
  while curr is not None:
    front = curr.next
    curr.next = prev
    curr.prev = front
    prev = curr
    curr = front
  temp = prev
  while temp is not None:
    print(temp.value, end=" ")
    temp = temp.next

reverse_doubly_LL(linkedList)
