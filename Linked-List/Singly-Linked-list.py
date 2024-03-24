# Singly Linked List Implementation... 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        if self.next is not None:
            del self.next
            self.next = None

def insert_at_tail(tail, d):
    # Creating a new Node
    temp = Node(d)

    tail.next = temp
    tail = temp
    return tail

def insert_at_head(head, d):
    temp = Node(d)
    temp.next = head
    head = temp
    return head

def insert_at_position(head, tail, position, d):
    # Inserting at Head
    if position == 1:
        return insert_at_head(head, d)

    temp = head
    cnt = 1

    while cnt < position - 1:
        temp = temp.next
        cnt += 1
    
    # Inserting at Tail
    if temp.next is None:
        return insert_at_tail(tail, d)

    node_to_insert = Node(d)
    node_to_insert.next = temp.next
    temp.next = node_to_insert
    return head

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
        prev.next = curr.next
        curr.next = None
        del curr
    return head, tail

def print_list(head):
    temp = head
    while temp is not None:
        print(" |", temp.data, "-->", temp.next, "| ", end="")
        temp = temp.next
    print()

def main():
    node1 = Node(10)
    head = node1
    tail = node1
    print_list(head)
    print("\nInsert At Head")
    head = insert_at_head(head, 12)
    print_list(head)
    print("\nInsert At Tail")
    tail = insert_at_tail(tail, 15)
    print_list(head)
    print("\nInsert At Position")
    head = insert_at_position(head, tail, 4, 20)
    print_list(head)

    print("Deleting Node")
    head, tail = delete_node(4, head, tail)
    print_list(head)
    print("Head:", head.data)
    print("Tail:", tail.data)

if __name__ == "__main__":
    main()
