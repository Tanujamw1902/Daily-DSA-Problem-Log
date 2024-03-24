# Spiral Matrix Problem... 

def spiral_matrix(arr):
    row_size = len(arr)
    col_size = len(arr[0])
    count = 0
    total = row_size * col_size

    startingRow = 0
    startingCol = 0
    endingRow = row_size - 1
    endingCol = col_size - 1

    while count < total:
        # Traverse the top row from left to right
        for index in range(startingCol, endingCol + 1):
            print(arr[startingRow][index], end=" ")
            count += 1
        startingRow += 1

        # Traverse the right column from top to bottom
        for index in range(startingRow, endingRow + 1):
            print(arr[index][endingCol], end=" ")
            count += 1
        endingCol -= 1

        # Traverse the bottom row from right to left
        for index in range(endingCol, startingCol - 1, -1):
            print(arr[endingRow][index], end=" ")
            count += 1
        endingRow -= 1

        # Traverse the left column from bottom to top
        for index in range(endingRow, startingRow - 1, -1):
            print(arr[index][startingCol], end=" ")
            count += 1
        startingCol += 1

def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    spiral_matrix(arr)

if __name__ == "__main__":
    main()
