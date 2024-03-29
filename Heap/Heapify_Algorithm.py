# Heapify Algorithm... 

class Heap:
    # Heapify Algorithm
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1  # Left child index in heap (Note: Indexing starts from 0)
        right = 2 * i + 2  # Right child index in heap (Note: Indexing starts from 0)

        # Check if left child is larger than root
        if left < n and arr[largest] < arr[left]:
            largest = left

        # Check if right child is larger than largest so far
        if right < n and arr[largest] < arr[right]:
            largest = right

        # If largest is not the root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    # Function to print an array
    def print_array(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    h = Heap()
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)

    print("Original array:", end=" ")
    h.print_array(arr)

    # Applying heapify on the whole array
    h.heapify(arr, n, 0)

    print("Heapified array:", end=" ")
    h.print_array(arr)
