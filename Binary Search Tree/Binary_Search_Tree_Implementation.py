# Binary Search Tree Implementation... 

from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_into_bst(root, d):
    if root is None:
        root = Node(d)
        return root
    if d > root.data:
        root.right = insert_into_bst(root.right, d)
    else:
        root.left = insert_into_bst(root.left, d)
    return root

def level_order_traversal(root):
    if root is None:
        return

    q = Queue()
    q.put(root)
    q.put(None)

    while not q.empty():
        temp = q.get()
        if temp is None:
            print()
            if not q.empty():
                q.put(None)
        else:
            print(temp.data, end=" ")
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)

def take_input():
    root = None
    data = int(input("Enter data (or -1 to stop): "))
    while data != -1:
        root = insert_into_bst(root, data)
        data = int(input("Enter data (or -1 to stop): "))
    return root

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)

def min_val(root):
    temp = root
    while temp.left is not None:
        temp = temp.left
    return temp

def delete_from_bst(root, val):
    if root is None:
        return root
    if root.data == val:
        if root.left is None and root.right is None:
            return None
        if root.left is not None and root.right is None:
            temp = root.left
            del root
            return temp
        if root.left is None and root.right is not None:
            temp = root.right
            del root
            return temp
        if root.left is not None and root.right is not None:
            mini = min_val(root.right).data
            root.data = mini
            root.right = delete_from_bst(root.right, mini)
            return root
    if val < root.data:
        root.left = delete_from_bst(root.left, val)
    else:
        root.right = delete_from_bst(root.right, val)
    return root

def max_val(root):
    temp = root
    while temp.right is not None:
        temp = temp.right
    return temp

def search_in_bst(root, x):
    if root is None:
        return False
    if root.data == x:
        return True
    if root.data > x:
        return search_in_bst(root.left, x)
    else:
        return search_in_bst(root.right, x)

if __name__ == "__main__":
    root = take_input()
    print("Printing The BST (Level Order Traversal)")
    level_order_traversal(root)

    print("\n\nInOrder Traversal")
    in_order(root)

    # Test Search
    print("\n\nSearch In BST")
    x = int(input("Enter a number to search: "))
    if search_in_bst(root, x):
        print(f"{x} is found in the BST.")
    else:
        print(f"{x} is not found in the BST.")

    # Print Min and Max Values
    print("\nMIN Value:")
    print(min_val(root).data)
    print("\nMAX Value:")
    print(max_val(root).data)

    # Test Delete
    x = int(input("\n\nEnter a value to delete from the BST: "))
    root = delete_from_bst(root, x)
    print("Printing The BST after deletion")
    level_order_traversal(root)
