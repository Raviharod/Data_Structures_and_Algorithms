'''Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.'''


import singlyLinkedList as sll
linkedList = sll.SinglyLinkedList()
linkedList.append(11)
linkedList.append(12)
linkedList.append(13)
linkedList.append(14)
linkedList.append(15)
linkedList.append(16)
linkedList.append(17)
linkedList.append(18)
linkedList.append(19)


#Brute force solution
def odd_even_LL(linkedList):
  curr = linkedList.head
  nums = []
  while curr is not None and curr.next is not None:
    nums.append(curr.value)
    curr = curr.next.next
  nums.append(curr.value)
  curr = linkedList.head.next
  while curr is not None and curr.next is not None:
    nums.append(curr.value)
    curr = curr.next.next
  # print(nums)
  curr = linkedList.head
  index = 0
  while curr is not None:
    curr.value = nums[index]
    curr = curr.next
    index += 1
  
  temp = linkedList.head
  while temp is not None:
    print(temp.value, end=" ")
    temp = temp.next
odd_even_LL(linkedList)


#optimal solution
def oddEvenLL(linkedList):
  if linkedList.head and linkedList.head.next is None:
    return linkedList.head
  odd = linkedList.head
  even = linkedList.head.next
  even_head = even
  while even is not None and even.next is not None:
    odd.next = odd.next.next
    odd = odd.next
    even.next = even.next.next
    even = even.next
  odd.next = even_head
  curr = linkedList.head
  while curr is not None:
    print(curr.value, end=" ")
    curr = curr.next

oddEvenLL(linkedList)


