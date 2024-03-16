# Kth Smallest Using Insertion Sort... 

def insertion_sort(arr, k):
    """
    Function to perform insertion sort and find the kth smallest element in an array.

    Args:
    - arr: The input array to be sorted.
    - k: The value of k.

    Returns:
    - The kth smallest element.
    """
    # Perform insertion sort
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    
    # Return the kth smallest element
    return arr[k - 1]

# Main function to test the insertion_sort function
if __name__ == "__main__":
    arr = [5, 3, 1, 8, 0]
    k = 2
    print(insertion_sort(arr, k))
