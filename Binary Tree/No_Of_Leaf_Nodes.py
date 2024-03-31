# No Of Leaf Nodes In Binary Tree... 

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

def count_leaf_nodes(root):
    count = 0
    if root is None:
        return count

    q = Queue()
    q.put(root)

    while not q.empty():
        temp = q.get()

        if temp.left is None and temp.right is None:
            count += 1

        if temp.left:
            q.put(temp.left)

        if temp.right:
            q.put(temp.right)

    return count

if __name__ == "__main__":
    root = build_tree()
    leaf_count = count_leaf_nodes(root)
    print("Number Of Leaf Nodes:", leaf_count)
