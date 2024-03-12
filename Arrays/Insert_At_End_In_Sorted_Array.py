# Insert an element at the end of the Sorted Array...

def insert_at_end_sorted(arr, element):
    # Find the index where the element should be inserted
    index = len(arr)
    # Insert the element at the end of the array
    arr.append(element)
    return index

# Example Usage
if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9]
    element = 8
    
    print("Array before insertion:", sorted_array)
    index = insert_at_end_sorted(sorted_array, element)
    print("Array after insertion at index", index, ":", sorted_array)
