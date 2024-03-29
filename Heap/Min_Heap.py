# Min Heap... 

import heapq  # Import the heapq module for the priority queue

# Initialize a list to store elements
min_heap = []

# Push elements into the min-heap
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 40)
heapq.heappush(min_heap, 50)
heapq.heappush(min_heap, 60)
heapq.heappush(min_heap, 70)
heapq.heappush(min_heap, 80)
heapq.heappush(min_heap, 90)
heapq.heappush(min_heap, 100)

# Top Element
print("Top element:", min_heap[0])  # The top element is at index 0

# Size Of Min Heap
print("Size of min heap:", len(min_heap))

# Empty Or Not
print("Is the min heap empty?", "Yes" if len(min_heap) == 0 else "No")

# Popping Some Element
heapq.heappop(min_heap)
print("Top element after popping:", min_heap[0])  # The new top element after popping is at index 0
