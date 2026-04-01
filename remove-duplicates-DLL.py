'''Remove duplicates from the doubly linked list
'''

import doublyLinkedList as DLL;
linkedList = DLL.DoublyLinkedList()
linkedList.append(1)
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(3)
linkedList.append(5)

#optimal solution
def removeDuplicates(linkedList):
  head = linkedList.head
  curr = head
  while curr is not None:
    if curr.prev and curr.prev.value == curr.value:
      if curr.prev == head:
        curr.prev = None
        head = curr
      else:
        curr.prev.prev.next = curr
        curr.prev = curr.prev.prev
    curr = curr.next

  curr = head
  while curr is not None:
    print(curr.value, end=" ")
    curr = curr.next

removeDuplicates(linkedList)