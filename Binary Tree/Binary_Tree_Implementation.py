# Binary Tree Implementation... 

from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree():
    print("Enter the data:")
    data = int(input())
    if data == -1:
        return None

    root = Node(data)

    print("Enter Data for inserting in left", data)
    root.left = build_tree()

    print("Enter Data for inserting in right", data)
    root.right = build_tree()

    return root

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)

def pre_order(root):
    if root is None:
        return
    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=" ")

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

def build_from_level_order():
    root_data = int(input("Enter Data For Root: "))
    if root_data == -1:
        return None

    root = Node(root_data)
    q = Queue()
    q.put(root)

    while not q.empty():
        temp = q.get()

        left_data = int(input("Enter Left Node For : " + str(temp.data)))
        if left_data != -1:
            temp.left = Node(left_data)
            q.put(temp.left)

        right_data = int(input("Enter Right Node For : " + str(temp.data)))
        if right_data != -1:
            temp.right = Node(right_data)
            q.put(temp.right)

    return root

if __name__ == "__main__":
    root = build_from_level_order()
    print("Printing Level Order Traversal")
    level_order_traversal(root)

    # Uncomment the below lines to test other traversals
    # print("\nInorder Traversal")
    # in_order(root)
    # print("\nPreorder Traversal")
    # pre_order(root)
    # print("\nPostorder Traversal")
    # post_order(root)
