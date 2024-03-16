# Sorting an Array... 

def bubble_sort(arr):
    """
    Function to perform bubble sort on an array.

    Args:
    - arr: The input array to be sorted.

    Returns:
    - None. The array is sorted in-place.
    """
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n - 1):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Main function to test the bubble_sort function
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    bubble_sort(arr)
    
    # Print the sorted array
    for i in range(len(arr)):
        print(arr[i], end=" ")
