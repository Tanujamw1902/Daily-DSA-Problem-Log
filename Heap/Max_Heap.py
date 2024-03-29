# Max Heap... 

import heapq

# Min-heap declaration
pq = []

# Push elements into the min-heap
heapq.heappush(pq, 10)
heapq.heappush(pq, 20)
heapq.heappush(pq, 30)
heapq.heappush(pq, 40)
heapq.heappush(pq, 50)
heapq.heappush(pq, 60)
heapq.heappush(pq, 70)
heapq.heappush(pq, 80)
heapq.heappush(pq, 90)
heapq.heappush(pq, 100)

# Top Element
print("Top element:", pq[0])

# Size Of Min Heap
print("Size of min heap:", len(pq))

# Empty Or Not
print("Is the min heap empty?", "Yes" if len(pq) == 0 else "No")

# Popping Some Element
heapq.heappop(pq)
print("Top element after popping:", pq[0])
