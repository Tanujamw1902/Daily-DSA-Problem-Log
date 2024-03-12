# Search in Unsorted Array...

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return its index
    return -1  # Element not found

# Example Usage
if __name__ == "__main__":
    unsorted_array = [9, 4, 7, 2, 5, 1, 8, 3, 6]
    target = 5
    
    index = linear_search(unsorted_array, target)
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the array.")
