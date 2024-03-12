# Array Reverse Using an Extra Array (Non In-place)...

def reverse_array(arr):
    reversed_arr = []
    # Iterate through the original array from end to start
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reversed_arr = reverse_array(arr)
    print("Original Array:", arr)
    print("Reversed Array:", reversed_arr)
