'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node. leetcode(876)'''

import singlyLinkedList as SLL

linkedList1 = SLL.SinglyLinkedList()
linkedList1.append(12)
linkedList1.append(13)
linkedList1.append(14)
linkedList1.append(15)
linkedList1.append(16)
linkedList1.append(17)
linkedList1.append(18)

#brute force approach
def findMiddle(linkList):
  count = 0
  curr = linkList.head.next
  while curr is not None:
    count += 1
    curr = curr.next
  high = 0
  if count%2 == 0:
    high = count//2
  else:
    high = count//2+1
  temp = linkList.head
  for _ in range(0,high):
    temp = temp.next
  print(temp.value)

# findMiddle(linkedList1)

#optimal solution
def findMiddleEl(linkedList):
  slow = linkedList.head
  fast = linkedList.head
  while slow is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
  return slow.value


print(findMiddleEl(linkedList1))