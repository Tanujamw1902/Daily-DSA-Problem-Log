# Finding An Element in Array... 

def find_element(arr, key):
    """
    Function to find the index of an element in an array.

    Args:
    - arr: The input array.
    - key: The element to search for.

    Returns:
    - The index of the element if found, otherwise -1.
    """
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if the current element matches the target element
        if arr[i] == key:
            # Return the index of the element
            return i
    
    # If the element is not found, return -1
    return -1

# Main function to test the find_element function
if __name__ == "__main__":
    # Input array
    arr = [1, 2, 3, 4, 5]
    # Element to search for
    key = 3
    
    # Call the find_element function and print the result
    print(find_element(arr, key))
