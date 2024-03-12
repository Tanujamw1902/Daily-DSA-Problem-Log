# Search operation in Sorted Array...

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

# Example Usage
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    
    index = binary_search(sorted_array, target)
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the array.")
