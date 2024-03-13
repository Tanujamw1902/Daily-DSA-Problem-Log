# Count Distinct (Unique) elements in an Array...

def countDistinct(arr):
    # Initialize a set to store unique elements
    unique_elements = set()
    
    # Iterate through the array
    for num in arr:
        # If the element is not already in the set, add it
        if num not in unique_elements:
            unique_elements.add(num)
    
    # Return the count of unique elements
    return len(unique_elements)

# Main function
if __name__ == "__main__":
    arr = [1, 2, 3, 3, 2, 1]
    print(countDistinct(arr))
