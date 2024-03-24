# Search In 2D Array Level 1 Problem... 

def search(arr, target):
    row_size = len(arr)
    col_size = len(arr[0])
    start = 0
    end = row_size * col_size - 1

    while start <= end:
        mid = start + (end - start) // 2
        element = arr[mid // col_size][mid % col_size]

        if element == target:
            print("Found")
            return

        if element < target:
            start = mid + 1
        else:
            end = mid - 1

    print("Not Found")

def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target = 5
    search(arr, target)

if __name__ == "__main__":
    main()
