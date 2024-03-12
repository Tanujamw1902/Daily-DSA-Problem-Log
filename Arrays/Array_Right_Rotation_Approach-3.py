# Array Right Rotation using Approach-3(Recursive Approach)...


def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rightRotate(arr, k):
    n = len(arr)
    k = k % n
    if k == 0:
        return  # If k is zero, no rotation is needed
    
    reverseArray(arr, 0, n - 1)  # Reverse the entire array
    reverseArray(arr, 0, k - 1)  # Reverse the first k elements
    reverseArray(arr, k, n - 1)  # Reverse the remaining elements

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
