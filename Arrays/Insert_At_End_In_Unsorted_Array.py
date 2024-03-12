# Insert an element at the end of an Unsorted Array...

def insert_at_end(arr, element):
    arr.append(element)

# Example Usage
if __name__ == "__main__":
    unsorted_array = [9, 4, 7, 2, 5, 1, 8, 3, 6]
    element = 10
    
    print("Array before insertion:", unsorted_array)
    insert_at_end(unsorted_array, element)
    print("Array after insertion:", unsorted_array)
