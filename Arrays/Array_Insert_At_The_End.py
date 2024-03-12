# Inserting an element at end of the Array...

# method to insert element
def insert(arr, element):
    arr.append(element)

# Example Usage
if __name__ == '__main__':
    # declaring array and key to insert
    arr = [12, 16, 20, 40, 50, 70]
    key = 26

    # array before inserting an element
    print("Before Inserting: ")
    print(arr)

    # array after inserting element
    insert(arr, key)
    print("After Inserting: ")
    print(arr)
