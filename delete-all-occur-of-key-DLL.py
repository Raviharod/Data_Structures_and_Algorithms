'''Delete all the occurrence of a key in a doubly linked list
ex: DLL [12,43,2,,43,2,11], key = 2
output = [12,43,43,11]
'''

import doublyLinkedList as DLL
linkedList = DLL.DoublyLinkedList()
linkedList.append(2)
linkedList.append(7)
linkedList.append(6)
linkedList.append(8)
linkedList.append(2)
linkedList.append(9)

#Optimal solution
def deleteKeys(linkedList, key):
  if linkedList.head.next is None and linkedList.head.value == key:
    return None
  temp = linkedList.head
  prev = None
  new_head = linkedList.head
  while temp is not None:
    if temp.value == key:
      if prev is not None:
        prev.next = temp.next
      if temp.next is not None:
        temp.next.prev = prev
      if temp == new_head:
        new_head = new_head.next
    prev = temp
    temp = temp.next
  while new_head is not None:
    print(new_head.value, end=" ")
    new_head = new_head.next

deleteKeys(linkedList, 2)