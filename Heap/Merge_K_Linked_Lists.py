# Merge K Linked Lists... 

import heapq


# Definition of Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a comparison function
class Compare:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.data < other.node.data

# Merge k sorted linked lists
def mergeKLists(lists):
    # Define min heap using heapq
    min_heap = []
    for head in lists:
        if head:
            heapq.heappush(min_heap, Compare(head))

    head = tail = None

    # Merge the lists
    while min_heap:
        top = heapq.heappop(min_heap).node

        if top.next:
            heapq.heappush(min_heap, Compare(top.next))

        if not head:
            head = tail = top
        else:
            tail.next = top
            tail = top

    return head

# Utility function to print the merged linked list
def printList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Testcase
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

head3 = Node(0)
head3.next = Node(7)
head3.next.next = Node(8)

listArray = [head1, head2, head3]

mergedHead = mergeKLists(listArray)

print("Merged Linked List:", end=" ")
printList(mergedHead)

# Free memory
current = mergedHead
while current:
    next_node = current.next
    del current
    current = next_node
