# Array Reverse Recursion (In-place or Non In-place)...

def reverse_array(arr):
    if len(arr) == 0:
        return []  # Base case: empty array
    return [arr[-1]] + reverse_array(arr[:-1])

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reversed_arr = reverse_array(arr)
    print("Original Array:", arr)
    print("Reversed Array:", reversed_arr)

# In-place (Modifying the Original Array)...

def reverse_array_inplace(arr, start, end):
    if start >= end:
        return  # Base case: start index is greater than or equal to end index
    
    # Swap elements at start and end indices
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recur for the rest of the array
    reverse_array_inplace(arr, start + 1, end - 1)

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original Array:", arr)
    reverse_array_inplace(arr, 0, len(arr) - 1)
    print("Reversed Array:", arr)
