# Kth Largest Subarray Approach-2... 

import heapq


def get_kth_largest(arr, k):
    min_heap = []
    n = len(arr)
    
    for i in range(n):
        subarray_sum = 0
        for j in range(i, n):
            subarray_sum += arr[j]
            if len(min_heap) < k:
                heapq.heappush(min_heap, subarray_sum)
            else:
                if subarray_sum > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, subarray_sum)
    
    return min_heap[0]

# Testcase
arr = [10, -10, 20, -20, 30, -30]
k = 3

print("Array:", arr)
result = get_kth_largest(arr, k)
print("Kth largest sum of subarrays:", result)
