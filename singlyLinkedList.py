#singly linked list implementation
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def append(self,value):
    newNode = Node(value)
    if self.head == None:
      self.head = newNode
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = newNode
  
  def traverse(self):
    if self.head is None:
      print("linked list is empty")
    else:
      curr = self.head
      while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print()
  def insertAtPos(self, value, position):
    new_node = Node(value)
    if position == 0:
      new_node.next = self.head
      self.head = new_node
    else:
      count = 0
      curr = self.head
      prev = None
      while curr is not None and count < position:
        prev = curr
        curr = curr.next
        count += 1
      prev.next = new_node
      new_node.next = curr
  
  def delete(self, value):
    temp = self.head
    if temp.next is not None:
      if value == temp.value:
        self.head = self.head.next
        temp.next = None
        del temp
      else:
        found = False
        prev = None
        while temp is not None:
          if temp.value == value:
            found = True
            break
          prev = temp
          temp = temp.next
        if found:
          prev.next = temp.next
          return
        else:
          print("Node not found")

