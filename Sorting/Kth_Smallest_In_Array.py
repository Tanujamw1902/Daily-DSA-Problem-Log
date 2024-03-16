# Finding Kth Smallest Element in an Array... 

def kth_smallest(arr, k):
    """
    Function to find the kth smallest element in an array.

    Args:
    - arr: The input array.
    - k: The value of k.

    Returns:
    - The kth smallest element.
    """
    # Loop through the array from index 0 to n - 2
    for i in range(len(arr) - 1):
        # Find the index of the minimum element in the unsorted portion of the array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the minimum element with the element at index i
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    # Return the kth smallest element
    return arr[k - 1]

# Main function to test the kth_smallest function
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    k = 3
    print(kth_smallest(arr, k))
