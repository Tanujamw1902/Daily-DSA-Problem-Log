# Rotate 2D Array 90 Deg... 

def rotate_array(arr):
    row_size = len(arr)
    col_size = len(arr[0])
    for col in range(col_size):
        for row in range(row_size - 1, -1, -1):
            print(" |", arr[row][col], "| ", end="")
        print()

def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Call the function to rotate the array
    rotate_array(arr)

if __name__ == "__main__":
    main()
