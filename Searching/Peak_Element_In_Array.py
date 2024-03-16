# Finding Peak Element in an Array... 

def binary_search(arr, low, high):
    """
    Function to perform binary search to find a peak element in an array.

    Args:
    - arr: The input array.
    - low: The lower index of the array.
    - high: The higher index of the array.

    Returns:
    - The index of the peak element.
    """
    while low <= high:
        mid = low + (high - low) // 2

        # Check if mid is a peak element
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return mid

        # If the element to the left of mid is greater, search in the left subarray
        if mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        # If the element to the right of mid is greater, search in the right subarray
        else:
            low = mid + 1

    return -1

# Main function to test the binary_search function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    low = 0
    high = len(arr) - 1
    print(binary_search(arr, low, high))
