# Insert an element at any position of an Unsorted Array...

def insert_at_position(arr, position, element):
    arr.insert(position, element)

# Example Usage
if __name__ == "__main__":
    unsorted_array = [9, 4, 7, 2, 5, 1, 8, 3, 6]
    position = 3
    element = 10
    
    print("Array before insertion:", unsorted_array)
    insert_at_position(unsorted_array, position, element)
    print("Array after insertion at position", position, ":", unsorted_array)
