# Kth Smallest Number... 

import heapq


def kth_smallest(arr, k):
    # Create a max heap to store the k smallest elements
    max_heap = []
    
    # Step 1: Push the first k elements into the max heap
    for i in range(k):
        heapq.heappush(max_heap, -arr[i])  # Push negative of element to simulate max heap
    
    # Step 2: Push remaining elements after comparing them with the top
    for i in range(k, len(arr)):
        if arr[i] < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -arr[i])  # Push negative of element to simulate max heap
    
    # Return the negative of the top element as it represents the kth smallest element
    return -max_heap[0]

# Test array
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# K value for testing
k = 3

# Test the function with the provided array and k value
print("Kth smallest element:", kth_smallest(arr, k))

# Test case 1: Array with negative numbers
arr2 = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
k = 5
print("Kth smallest element in array with negative numbers:", kth_smallest(arr2, k))

# Test case 2: Array with repeated elements
arr3 = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
k = 2
print("Kth smallest element in array with repeated elements:", kth_smallest(arr3, k))

# Test case 3: K equals 1
k = 1
print("Kth smallest element when k equals 1:", kth_smallest(arr, k))

# Test case 4: K equals size of the array
k = len(arr)
print("Kth smallest element when k equals the size of the array:", kth_smallest(arr, k))
