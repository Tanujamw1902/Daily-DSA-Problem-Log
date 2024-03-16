# Program for two sum in hash table...

def two_sum(nums, target):
    # Dictionary to store the complement of each number and its index
    num_dict = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement required to reach the target
        complement = target - num
        
        # If the complement exists in the dictionary, return its index and the current index
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Otherwise, add the current number and its index to the dictionary
        num_dict[num] = i

    # If no solution is found, return an empty list
    return []

# Main function to test the two_sum function
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    indices = two_sum(nums, target)
    
    # Print the indices of the two numbers that add up to the target
    if indices:
        print("Indices:", indices[0], ",", indices[1])
    else:
        print("No solution found.")
