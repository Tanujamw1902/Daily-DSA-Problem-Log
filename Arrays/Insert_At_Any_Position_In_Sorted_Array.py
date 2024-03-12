# Insert an element at any position in the Sorted Array...

def insert_at_position_sorted(arr, element):
    # Find the index where the element should be inserted
    index = 0
    while index < len(arr) and arr[index] < element:
        index += 1
    # Insert the element at the found index
    arr.insert(index, element)
    return index

# Example Usage
if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9]
    element = 4
    
    print("Array before insertion:", sorted_array)
    index = insert_at_position_sorted(sorted_array, element)
    print("Array after insertion at index", index, ":", sorted_array)
