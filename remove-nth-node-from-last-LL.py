'''Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 '''
import singlyLinkedList as LL
linkedList = LL.SinglyLinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)
linkedList.append(23)
linkedList.append(12)
linkedList.append(11)


#Brute force approach
def removeNth(linkedList, n):
  if linkedList.head.next is None and n == 1:
    linkedList.head = None
    return
  count = 0
  curr = linkedList.head
  while curr is not None:
    count += 1
    curr = curr.next
  
  if count == n:
    temp = linkedList.head.next
    linkedList.head = temp
  index = count - n
  temp = 1
  curr = linkedList.head
  while curr is not None:
    if temp == index:
      curr.next = curr.next.next
      break
    else:
      curr = curr.next
      temp += 1
  curr = linkedList.head
  while curr is not None:
    print(curr.value, end=" ")
    curr = curr.next
  
removeNth(linkedList, 1)


#optimal solution
def remove_nth_node(linkedList, n):
  slow = linkedList.head
  fast = linkedList.head
  for _ in range(n):
    fast = fast.next
  if fast == None:
    return linkedList.head.next
  while fast.next is not None:
    slow = slow.next
    fast = fast.next
  slow.next = slow.next.next
  curr = linkedList.head
  while curr is not None:
    print(curr.value, end=" ")
    curr = curr.next
  
remove_nth_node(linkedList, 2)
