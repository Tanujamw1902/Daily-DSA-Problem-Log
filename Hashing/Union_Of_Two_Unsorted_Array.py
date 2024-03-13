# Program for Two Unsorted Array...

def print_union(a, b):
    # Create a set to store unique elements from both arrays
    union_set = set()

    # Add elements from the first array to the set
    for num in a:
        union_set.add(num)

    # Add elements from the second array to the set
    for num in b:
        union_set.add(num)

    # Print the elements of the set (which are distinct elements of both arrays)
    for num in union_set:
        print(num, end=" ")

# Main function
if __name__ == "__main__":
    a = [1, 2, 23, 3, 4, 5, 4]
    b = [12, 23, 4, 3, 1]
    print_union(a, b)
