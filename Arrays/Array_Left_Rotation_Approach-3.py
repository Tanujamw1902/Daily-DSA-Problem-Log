# Array Left Rotation using Approach-3(A Jaggling Method)...

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
    # Normalize d to be within the range of array size
    d = d % n
    # Find the greatest common divisor of d and n
    g_c_d = gcd(d, n)
    # Iterate through each block
    for i in range(g_c_d):
        # Store the value of the i-th element of the array
        temp = arr[i]
        j = i
        # Move elements within the block to their new positions
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        # Put the stored value in its final position
        arr[j] = temp

# UTILITY FUNCTIONS
# Function to print an array
def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")

# Function to get gcd of a and b
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example Usage
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    d = 2
    
    # Print original array
    print("Original Array:")
    printArray(arr, n)
    print("\n")
    
    # Rotate the array
    leftRotate(arr, d, n)
    
    # Print rotated array
    print("Array after rotating by", d, "elements:")
    printArray(arr, n)
