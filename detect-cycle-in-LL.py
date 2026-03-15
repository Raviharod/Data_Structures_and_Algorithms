#detect the cycle in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Create a cycle
    def create_cycle(self, pos):
        temp = self.head
        cycle_node = None
        count = 0

        while temp.next:
            if count == pos:
                cycle_node = temp
            temp = temp.next
            count += 1

        temp.next = cycle_node 


# Create linked list
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

# Create cycle (last node points to node at index 1)
ll.create_cycle(1)

slow = ll.head
fast = ll.head
while fast is not None and fast.next is not None:
    slow = slow.next 
    fast = fast.next.next
    if slow == fast:
        slow = ll.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        print(slow)
else:
    print(None)
