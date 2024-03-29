# Min Max Segment... 

import sys


# Function to build the segment tree
def build(node, st, en):
    if st == en:
        tree[node] = a[st]
        return

    mid = (st + en) // 2
    build(2 * node, st, mid)
    build(2 * node + 1, mid + 1, en)

    tree[node] = max(tree[2 * node], tree[2 * node + 1])

# Function to query the segment tree
def query(node, st, en, l, r):
    if st > r or en < l:
        return -sys.maxsize - 1
    if l <= st and en <= r:
        return tree[node]

    mid = (st + en) // 2
    q1 = query(2 * node, st, mid, l, r)
    q2 = query(2 * node + 1, mid + 1, en, l, r)
    return max(q1, q2)

# Function to update a value in the segment tree
def update(node, st, en, idx, val):
    if st == en:
        a[st] = val
        tree[node] = val
        return

    mid = (st + en) // 2
    if idx <= mid:
        update(2 * node, st, mid, idx, val)
    else:
        update(2 * node + 1, mid + 1, en, idx, val)
    tree[node] = max(tree[2 * node], tree[2 * node + 1])

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

    # Build segment tree
    build(1, 0, n - 1)

    # Print segment tree
    print("Segment Tree:", end=" ")
    for i in range(4 * n - 1):
        print(tree[i], end=" ")
    print()

    # Handle queries and updates
    while True:
        type = int(input("\nEnter Type (-1 to exit, 1 for query, 2 for update): "))

        if type == -1:
            break
        if type == 1:
            l, r = map(int, input("Enter l and r: ").split())
            ans = query(1, 0, n - 1, l, r)
            print("Query Result:", ans)
        elif type == 2:
            idx, val = map(int, input("Enter index and value to update: ").split())
            update(1, 0, n - 1, idx, val)
            print("Updated Segment Tree:", end=" ")
            for i in range(4 * n - 1):
                print(tree[i], end=" ")
            print()

