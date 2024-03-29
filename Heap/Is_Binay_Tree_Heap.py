# Is Binary Tree Heap... 

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def is_CBT(root, index, cnt):
    if root is None:
        return True
    if index >= cnt:
        return False
    left = is_CBT(root.left, 2 * index + 1, cnt)
    right = is_CBT(root.right, 2 * index + 2, cnt)
    return left and right

def is_max_order(root):
    if root.left is None and root.right is None:
        return True
    if root.right is None:
        return root.data >= root.left.data
    left = is_max_order(root.left)
    right = is_max_order(root.right)
    return left and right and root.data >= root.left.data and root.data >= root.right.data

def is_heap(tree):
    index = 0
    total_count = count_nodes(tree)
    if is_CBT(tree, index, total_count) and is_max_order(tree):
        return True
    return False

def print_result(tree):
    if is_heap(tree):
        print("The binary tree is a heap.")
    else:
        print("The binary tree is not a heap.")

# Test cases
root1 = Node(10)
root1.left = Node(5)
root1.right = Node(7)

print("Test case 1:")
print_result(root1)  # Should output "The binary tree is a heap."

root2 = Node(10)
root2.left = Node(15)
root2.right = Node(20)

print("\nTest case 2:")
print_result(root2)  # Should output "The binary tree is not a heap."

root3 = Node(20)
root3.left = Node(15)
root3.right = Node(10)
root3.left.left = Node(12)
root3.left.right = Node(14)
root3.right.left = Node(8)

print("\nTest case 3:")
print_result(root3)  # Should output "The binary tree is a heap."
