# Implement Insertion Sort For Sorting Array In Non Decreasing Order... 

def insertion_sort(arr):
    """
    Function to perform insertion sort for sorting an array in non-decreasing order.

    Args:
    - arr: The input array to be sorted.

    Returns:
    - None. The array is sorted in-place.
    """
    # Traverse through the array starting from the second element
    for i in range(1, len(arr)):
        # Store the current element in a temporary variable
        temp = arr[i]

        # Initialize j to i-1
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than temp,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the temporary element at its correct position
        arr[j + 1] = temp

# Main function to test the insertion_sort function
if __name__ == "__main__":
    arr = [5, 3, 1, 8, 0]

    print("*** Before Sorting ***")
    for num in arr:
        print(num, end=" ")
    
    insertion_sort(arr)

    print("\n*** After Sorting ***")
    for num in arr:
        print(num, end=" ")
