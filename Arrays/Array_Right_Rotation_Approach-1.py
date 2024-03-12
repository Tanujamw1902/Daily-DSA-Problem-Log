# Array Right Rotation using Approach-1(Using Formula Basis)...

# Function to rightRotate array
def RightRotate(a, n, k):
    # If rotation is greater than size of array
    k = k % n
    # Iterate through the array
    for i in range(0, n):
        if(i < k):
            # Printing rightmost kth elements
            print(a[n + i - k], end=" ")
        else:
            # Prints array after 'k' elements
            print(a[i - k], end=" ")
    print("\n")

# Example Usage
if __name__ == "__main__":
    Array = [1, 2, 3, 4, 5]
    N = len(Array)
    K = 2
    
    # Print original array
    print("Original Array:")
    for i in Array:
        print(i, end=" ")
    print("\n")
    
    # Right rotate the array
    print("Array after right rotation by", K, "elements:")
    RightRotate(Array, N, K)
