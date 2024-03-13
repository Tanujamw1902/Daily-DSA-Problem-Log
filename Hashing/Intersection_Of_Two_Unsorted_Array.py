# Intersection of two Unsorted Arrays...

def print_intersection(a, b):
    # Convert the first array into a set
    set_a = set(a)
    
    # Initialize a set to store the intersection elements
    intersection = set()

    # Iterate through the second array
    for num in b:
        # If the element is found in the set_a, add it to the intersection set and remove it from set_a
        if num in set_a:
            intersection.add(num)
            set_a.remove(num)
    
    # Print the intersection elements
    for num in intersection:
        print(num, end=" ")

# Main function
if __name__ == "__main__":
    a = [1, 2, 23, 3, 4, 5, 4]
    b = [12, 23, 4, 3, 1]
    print_intersection(a, b)
