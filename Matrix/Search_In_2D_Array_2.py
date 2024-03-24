# Search In 2D Array Level 2 Problem... 

def search(arr, target):
    row_size = len(arr)
    col_size = len(arr[0])
    row = 0
    col = col_size - 1

    while row < row_size and col >= 0:
        element = arr[row][col]

        if element == target:
            print("Found")
            return

        if element < target:
            row += 1
        else:
            col -= 1

    print("Not Found")

def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target = 5
    search(arr, target)

if __name__ == "__main__":
    main()
