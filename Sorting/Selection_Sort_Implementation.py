# Implement Selection Sort for Sorting an Array In Non Decreasing Order... 

def selection_sort(arr):
    """
    Function to perform selection sort for sorting an array in non-decreasing order.

    Args:
    - arr: The input array to be sorted.

    Returns:
    - None. The array is sorted in-place.
    """
    # Traverse through the array
    for i in range(len(arr)):
        # Find the index of the minimum element in the unsorted portion of the array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Main function to test the selection_sort function
if __name__ == "__main__":
    arr = [5, 3, 1, 8, 0]
    
    print("*** Before Sorting ***")
    for num in arr:
        print(num, end=" ")
    
    selection_sort(arr)

    print("\n*** After Sorting ***")
    for num in arr:
        print(num, end=" ")
