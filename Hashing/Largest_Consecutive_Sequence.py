# Program for Largest Consecutive Sequence in Hash Table... 

def longest_consecutive(nums):
    # Convert the list to a set for faster lookup
    num_set = set(nums)

    # Initialize the variable to store the length of the longest consecutive sequence
    longest_sequence = 0

    # Iterate through each number in the list
    for num in nums:
        # Check if the current number is the start of a consecutive sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            # Continue checking for consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            # Update the longest_sequence if the current sequence is longer
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence

# Main function to test the longest_consecutive function
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    longest = longest_consecutive(nums)
    
    # Print the length of the longest consecutive sequence
    print("Longest Consecutive Sequence Length Is:", longest)
