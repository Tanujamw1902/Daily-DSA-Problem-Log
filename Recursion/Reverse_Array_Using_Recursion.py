# Program for Reverse Array Using Recursion...

# Function to reverse an array using recursion
def reverse_array(arr, start, end):
    # Base case: if start index surpasses end index, return
    if start >= end:
        return
    
    # Swap elements at start and end indices
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursive call with incremented start index and decremented end index
    reverse_array(arr, start + 1, end - 1)

# Example array
arr = [1, 2, 3, 4, 5]

# Display original array
print("Original array:", arr)

# Call the reverse_array function
reverse_array(arr, 0, len(arr) - 1)

# Display reversed array
print("Reversed array:", arr)
