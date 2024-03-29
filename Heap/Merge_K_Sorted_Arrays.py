# Merge K Sorted Arrays... 

import heapq


# Define a class for node
class Node:
    def __init__(self, data, row, col):
        self.data = data
        self.row = row
        self.col = col

# Define a comparison function
class Compare:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.data < other.node.data

def mergeKSortedArrays(kArrays):
    # Define min heap using heapq
    min_heap = []
    for i in range(len(kArrays)):
        if kArrays[i]:
            heapq.heappush(min_heap, Compare(Node(kArrays[i][0], i, 0)))

    ans = []
    while min_heap:
        tmp = min_heap[0].node

        ans.append(tmp.data)
        heapq.heappop(min_heap)
        i, j = tmp.row, tmp.col

        if j + 1 < len(kArrays[i]):
            heapq.heappush(min_heap, Compare(Node(kArrays[i][j + 1], i, j + 1)))

    return ans

# Testcase
kArrays = [[1, 3, 5], [2, 4, 6], [0, 7, 8]]
result = mergeKSortedArrays(kArrays)

print("Merged sorted array:", result)
