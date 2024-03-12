# Array Reverse Stack (Non In-place)...

def reverse_array_stack(arr):
    stack = []
    reversed_arr = []
    
    # Push elements of the array onto the stack
    for num in arr:
        stack.append(num)
    
    # Pop elements from the stack to construct the reversed array
    while stack:
        reversed_arr.append(stack.pop())
    
    return reversed_arr

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reversed_arr = reverse_array_stack(arr)
    print("Original Array:", arr)
    print("Reversed Array using stack:", reversed_arr)
