# Array Reverse Using a Loop (In-place)...

def reverse_array_inplace(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        # Swap elements at start and end indices
        arr[start], arr[end] = arr[end], arr[start]
        # Move start index forward
        start += 1
        # Move end index backward
        end -= 1

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original Array:", arr)
    reverse_array_inplace(arr)
    print("Reversed Array:", arr)
