# Merge Two Binary Max Heaps... 

# Function to heapify an array
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

# Function to merge two max heaps
def mergeHeaps(a, b):
    ans = []

    # Merge the two heaps
    ans.extend(a)
    ans.extend(b)

    # Heapify the merged heap
    size = len(ans)
    for i in range(size // 2 - 1, -1, -1):
        heapify(ans, size, i)

    # Output the merged heap (optional)
    print("Merged Max Heap:", ans)

    return ans

# Test cases
a = [10, 7, 5, 4, 3]
b = [9, 8, 6, 2, 1]

print("Heap A:", a)
print("Heap B:", b)

mergedHeap = mergeHeaps(a, b)
