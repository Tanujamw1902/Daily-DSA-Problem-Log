# Kth - Smallest Using Selection Sort... 

def selection_sort(arr, k):
    """
    Function to perform selection sort and find the kth smallest element in an array.

    Args:
    - arr: The input array to be sorted.
    - k: The value of k.

    Returns:
    - The kth smallest element.
    """
    # Perform selection sort
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    # Return the kth smallest element
    return arr[k - 1]

# Main function to test the selection_sort function
if __name__ == "__main__":
    arr = [5, 3, 1, 8, 0]
    k = 2
    print(selection_sort(arr, k))
