# Program for Searching in Sorted Array... 

def binary_search(arr, low, high, key):
    """
    Function to perform binary search on a sorted array.

    Args:
    - arr: The sorted array.
    - low: The lower index of the array.
    - high: The higher index of the array.
    - key: The element to search for.

    Returns:
    - The index of the key if found, otherwise -1.
    """
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    # If the key is not found, return -1
    return -1

# Main function to test the binary_search function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    key = 1
    low = 0
    high = n - 1
    print(binary_search(arr, low, high, key))
