#find the length of the cycle involved in a linked list
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



#Brute force approach
def find_length(linkedList):
    temp = None
    curr = linkedList.head
    my_set = set()
    while curr is not None:
        # print(curr.data)
        if curr in my_set:
            temp = curr
            break
        my_set.add(curr)
        curr = curr.next
    
    count = 0
    curr1 = linkedList.head
    while curr1 is not None:
        if curr1 == temp:
            # print(curr1.data, temp.data)
            demo = curr1.next
            while demo != temp:
                # print(count)
                count += 1
                demo = demo.next
            break
        curr1 = curr1.next
    return count+1
print(find_length(ll))
    
#Better Solution
def findLength(linkedList):
    temp = linkedList.head
    travel = 0
    my_dict = {}
    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]
        
        my_dict[temp] = travel
        travel += 1
        temp = temp.next

    return "The given Linked list does not have cycle"

print(findLength(ll))


#optimal solution
def find_length_LL(linkedList):
    slow = linkedList.head
    fast = linkedList.head
    count = 1
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            while slow != fast:
                count += 1
                slow = slow.next
            return count
    return count
print(find_length_LL(ll))