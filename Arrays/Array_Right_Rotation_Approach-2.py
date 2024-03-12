# Array Right Rotation using Approach-2(Reversing the Array)...

# Function to reverse the elements of an array within a given range
def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # Swap elements at start and end indices
        start += 1  # Move start index forward
        end -= 1  # Move end index backward

# Function to right rotate array by k elements
def rightRotate(arr, k):
    n = len(arr)  # Get the size of the array
    k = k % n  # Ensure k is within the range of array size
    
    # Reverse the last k elements
    reverseArray(arr, n - k, n - 1)
    # Reverse the first n-k elements
    reverseArray(arr, 0, n - k - 1)
    # Reverse the entire array
    reverseArray(arr, 0, n - 1)

# Example Usage
if __name__ == "__main__":
    Array = [1, 2, 3, 4, 5]
    K = 2
    
    # Print original array
    print("Original Array:", Array)
    
    # Right rotate the array
    rightRotate(Array, K)
    
    # Print array after rotation
    print("Array after right rotation by", K, "elements:", Array)
