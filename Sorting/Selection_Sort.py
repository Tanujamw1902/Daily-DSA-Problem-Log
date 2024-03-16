# Selection Sort... 

def selection_sort(arr):
    """
    Function to perform selection sort.

    Args:
    - arr: The input array to be sorted.

    Returns:
    - None. The array is sorted in-place.
    """
    # Traverse through the array
    for i in range(len(arr) - 1):
        # Find the index of the minimum element in the unsorted portion of the array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Main function to test the selection_sort function
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]

    # Call the selection_sort function
    selection_sort(arr)

    # Print the sorted array
    for num in arr:
        print(num, end=" ")
