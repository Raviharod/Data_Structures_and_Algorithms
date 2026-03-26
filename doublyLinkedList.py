'''Implementing the doubly linked list'''

class Node:
  def __init__(self, value):
    self.prev = None
    self.value = value
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def insert_at_head(self,value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
  
  def append(self,value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = new_node
      new_node.prev = curr
  
  def insert_at_pos(self,value,pos):
    new_node = Node(value)
    if pos == 0:
      self.insert_at_head(value)
      return
    curr = self.head
    count = 0
    while curr is not None and count < pos-1:
      curr = curr.next
      count += 1
    if curr == None:
      return "position is out of bounds"
    new_node.prev = curr
    new_node.next = curr.next
    if curr.next is not None:
      curr.next.prev = new_node
    curr.next = new_node
  
  def traverse(self):
    curr = self.head
    if curr is not None:
      print(curr.value, end=" ")
      curr = curr.next
  


# DLL = DoublyLinkedList()
# DLL.append(1)
# DLL.append(2)
# DLL.append(3)
# DLL.append(4)
# DLL.append(5)
# DLL.insert_at_pos(23,3)

