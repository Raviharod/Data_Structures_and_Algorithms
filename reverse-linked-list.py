#Given the head of a singly linked list, reverse the list, and return the reversed list.

import singlyLinkedList as SLL

linkedList = SLL.SinglyLinkedList()
linkedList.append(5)
linkedList.append(8)
linkedList.append(7)
linkedList.append(3)
linkedList.append(2)

#Brute force approach
def reverseLL(linkedList):
  arr = []
  curr = linkedList.head
  while curr is not None:
    arr.append(curr.value)
    curr = curr.next
  n = len(arr)
  tempUpd = linkedList.head
  for i in range(n-1, -1, -1):
    tempUpd.value = arr[i]
    tempUpd = tempUpd.next
  temp =linkedList.head
  while temp is not None:
    print(temp.value, end=" ")
    temp = temp.next
reverseLL(linkedList)

#Another brute force solution
def reverseLinkedList(linkedList):
  temp = linkedList.head
  tempList = []
  while temp is not None:
    tempList.append(temp.value)
    temp = temp.next
  
  temp1 = linkedList.head
  while temp1 is not None:
    temp1.value = tempList.pop()
    temp1 = temp1.next
  temp2 =linkedList.head
  while temp2 is not None:
    print(temp2.value, end=" ")
    temp2 = temp2.next
reverseLinkedList(linkedList)

#Optimal Solution
def reverse_Linked_list(linkedList):
  prev = None
  temp = linkedList.head
  while temp is not None:
    front = temp.next
    temp.next = prev
    prev = temp
    temp = front
  temp2 = prev
  while temp2 is not None:
    print(temp2.value, end=" ")
    temp2 = temp2.next
    



reverse_Linked_list(linkedList)