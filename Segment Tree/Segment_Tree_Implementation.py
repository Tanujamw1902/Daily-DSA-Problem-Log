# Segment Tree Implementation... 

def build(node, st, en):
    if st == en:
        tree[node] = a[st]
        return

    mid = (st + en) // 2
    build(2 * node, st, mid)
    build(2 * node + 1, mid + 1, en)

    tree[node] = tree[2 * node] + tree[2 * node + 1]

if __name__ == "__main__":
    N = 100002  # Maximum array size
    a = [0] * N  # Array
    tree = [0] * (4 * N)  # Segment Tree

    # Input size of array
    n = int(input("Enter Size Of Array: "))

    # Input numbers
    print("Enter Numbers:")
    for i in range(n):
        a[i] = int(input())

    build(1, 0, n - 1)

    # Printing Segment Tree
    print("Printing Segment Tree:")
    for i in range(4 * n):
        print(tree[i], end=" ")
