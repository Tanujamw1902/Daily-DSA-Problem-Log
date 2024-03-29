# Heap Sort... 

class Heap:
    # Function to heapify a subtree rooted at index i.
    # n is the size of the heap
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # If left child is larger than root
        if left < n and arr[largest] < arr[left]:
            largest = left

        # If right child is larger than largest so far
        if right < n and arr[largest] < arr[right]:
            largest = right

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    # Main function to perform heap sort
    def heap_sort(self, arr):
        n = len(arr)

        # Build a maxheap.
        # Since the last non-leaf node will be at (n//2)-1 index,
        # start from this node and go up to the root (index 0).
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            # Swap the current root (maximum value) with the last element
            arr[i], arr[0] = arr[0], arr[i]
            # Call heapify on the reduced heap
            self.heapify(arr, i, 0)

    # Function to print an array
    def print_array(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    h = Heap()
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", end=" ")
    h.print_array(arr)

    h.heap_sort(arr)

    print("Sorted array:", end=" ")
    h.print_array(arr)
