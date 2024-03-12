# Array Left Rotation using an Approach-2(Rotate one by one)...

# Function to left rotate arr[] of size n by d
def Rotate(arr, d, n):
    # Loop to rotate the array d times
    p = 1
    while(p <= d):
        last = arr[0]
        # Shift elements to the left by one position
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        # Place the last element at the end
        arr[n - 1] = last
        p += 1

# Function to print an array
def printArray(arr, size):
    # Loop to print each element of the array
    for i in range(size):
        print(arr[i], end=" ")

# Example Usage
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    N = len(arr)
    d = 2

    # Print original array
    print("Original Array:")
    printArray(arr, N)
    print("\n")

    # Rotate the array
    Rotate(arr, d, N)

    # Print rotated array
    print("Array after rotating by", d, "elements:")
    printArray(arr, N)
