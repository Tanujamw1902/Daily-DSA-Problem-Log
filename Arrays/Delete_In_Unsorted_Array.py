# Delete operation in Unsorted Array...

def delete_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            arr.pop(i)
            return True  # Element deleted successfully
    return False  # Element not found

# Example Usage
if __name__ == "__main__":
    unsorted_array = [9, 4, 7, 2, 5, 1, 8, 3, 6]
    target = 5
    
    print("Array before deletion:", unsorted_array)
    if delete_element(unsorted_array, target):
        print("Element", target, "deleted successfully.")
    else:
        print("Element", target, "not found in the array.")
    print("Array after deletion:", unsorted_array)
