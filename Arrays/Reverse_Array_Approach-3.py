# Array Reverse Inbuilt Methods (Non In-place)...

def reverse_array(arr):
    return list(reversed(arr))

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reversed_arr = reverse_array(arr)
    print("Original Array:", arr)
    print("Reversed Array:", reversed_arr)

# Using slicing:

def reverse_array(arr):
    return arr[::-1]

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reversed_arr = reverse_array(arr)
    print("Original Array:", arr)
    print("Reversed Array:", reversed_arr)
