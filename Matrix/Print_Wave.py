# Print Wave Problem... 

def print_wave(arr):
    # Loop through each column
    for col in range(len(arr[0])):
        # For odd columns, print elements from bottom to top
        if col % 2 == 1:
            for row in range(len(arr) - 1, -1, -1):
                print(arr[row][col], end=" ")
        # For even columns, print elements from top to bottom
        else:
            for row in range(len(arr)):
                print(arr[row][col], end=" ")
        print()  # Move to the next line after printing each column

def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    row_size = len(arr)
    col_size = len(arr[0])

    # Call the function to print the array in wave pattern
    print_wave(arr)

    # Printing Array
    # Uncomment the following lines to print the array normally
    # for row in range(row_size):
    #     for col in range(col_size):
    #         print(arr[row][col], end=" ")
    #     print()

if __name__ == "__main__":
    main()
