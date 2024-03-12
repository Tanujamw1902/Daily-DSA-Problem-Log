# Delete operation in Sorted Array..

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Element not found

def delete_element(arr, target):
    index = binary_search(arr, target)
    if index != -1:
        # Shift elements to the left to remove the target element
        for i in range(index, len(arr) - 1):
            arr[i] = arr[i + 1]
        # Remove the last element (duplicated after shifting)
        arr.pop()
        return True  # Element deleted successfully
    else:
        return False  # Element not found

# Example Usage
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    
    print("Array before deletion:", sorted_array)
    if delete_element(sorted_array, target):
        print("Element", target, "deleted successfully.")
    else:
        print("Element", target, "not found in the array.")
    print("Array after deletion:", sorted_array)
