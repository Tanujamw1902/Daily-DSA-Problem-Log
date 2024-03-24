# Doubly Linked List Implementation... 

class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None

def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def insert_at_head(head, tail, d):
    if head is None:
        temp = Node(d)
        head = temp
        tail = temp
    else:
        temp = Node(d)
        temp.next = head
        head.prev = temp
        head = temp
    return head, tail

def insert_at_tail(head, tail, d):
    if tail is None:
        temp = Node(d)
        head = temp
        tail = temp
    else:
        temp = Node(d)
        tail.next = temp
        temp.prev = tail
        tail = temp
    return head, tail

def insert_at_position(head, tail, position, d):
    # Inserting at Head
    if position == 1:
        return insert_at_head(head, tail, d)

    temp = head
    cnt = 1
    while cnt < position - 1:
        temp = temp.next
        cnt += 1
    
    # Inserting at Tail
    if temp.next is None:
        return insert_at_tail(head, tail, d)

    node_to_insert = Node(d)
    node_to_insert.next = temp.next
    temp.next.prev = node_to_insert
    temp.next = node_to_insert
    node_to_insert.prev = temp
    return head, tail

def delete_node(position, head, tail):
    if position == 1:
        temp = head
        head = head.next
        temp.next = None
        del temp
    else:
        curr = head
        prev = None
        cnt = 1
        while cnt < position:
            prev = curr
            curr = curr.next
            cnt += 1
        if curr.next is None:
            tail = prev
        curr.prev = None
        prev.next = curr.next
        curr.next = None
        del curr
    return head, tail

def get_length(head):
    length = 0
    temp = head
    while temp is not None:
        length += 1
        temp = temp.next
    return length

def main():
    node1 = Node(10)
    head = node1
    tail = node1
    head, tail = insert_at_head(head, tail, 11)
    head, tail = insert_at_head(head, tail, 12)
    head, tail = insert_at_head(head, tail, 13)
    head, tail = insert_at_head(head, tail, 14)
    head, tail = insert_at_tail(head, tail, 15)
    head, tail = insert_at_position(head, tail, 7, 20)
    print_list(head)
    print()
    head, tail = delete_node(7, head, tail)
    print_list(head)

if __name__ == "__main__":
    main()
