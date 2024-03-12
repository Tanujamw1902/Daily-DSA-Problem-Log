# Array Left Rotation using an Approach-1(using temp array)...

def rotate(L, d, n):
    d = d % n
    k = L.index(d)
    new_lis = L[k + 1:] + L[0:k + 1]
    return new_lis

# Example Usage
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    N = len(arr)

    # Rotate the array
    arr = rotate(arr, d, N)

    # Print the rotated array
    for i in arr:
        print(i, end=" ")
