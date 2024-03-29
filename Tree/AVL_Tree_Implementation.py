# AVL Tree Implementation... 

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of the node

def height(node):
    # Function to calculate the height of the node
    if node is None:
        return 0
    return node.height

def max(a, b):
    # Function to find the maximum of two numbers
    return a if a > b else b

def newNode(key):
    # Function to create a new node
    node = Node(key)
    return node

def rightRotate(y):
    # Right rotation operation
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1

    return x

def leftRotate(x):
    # Left rotation operation
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1

    return y

def getBalance(N):
    # Function to get the balance factor of a node
    if N is None:
        return 0
    return height(N.left) - height(N.right)

def insert(node, key):
    # Function to insert a new node into the AVL tree
    if node is None:
        return newNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    node.height = 1 + max(height(node.left), height(node.right))

    balance = getBalance(node)

    # If the node becomes unbalanced, perform rotations
    if balance > 1 and key < node.left.key:
        return rightRotate(node)

    if balance < -1 and key > node.right.key:
        return leftRotate(node)

    if balance > 1 and key > node.left.key:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    if balance < -1 and key < node.right.key:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node

def preOrder(root):
    # Preorder traversal of the AVL tree
    if root is not None:
        print(root.key, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def printAVLTree(root, indent="", last=True):
    # Print AVL tree structure
    if root is not None:
        print(indent, end="")
        if last:
            print("R----", end="")
            indent += "     "
        else:
            print("L----", end="")
            indent += "|    "

        print(root.key)

        printAVLTree(root.left, indent, False)
        printAVLTree(root.right, indent, True)

# Main function
if __name__ == "__main__":
    root = None

    # Test cases
    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        root = insert(root, key)

    print("Preorder traversal of AVL tree after insertion:", end=" ")
    preOrder(root)
    print()

    print("AVL tree structure:")
    printAVLTree(root)
