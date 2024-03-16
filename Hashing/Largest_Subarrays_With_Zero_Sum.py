# Program for Largest subarrays with zero sum... 

def largest_subarray_with_zero_sum(nums):
    # Dictionary to store the prefix sum and its corresponding index
    prefix_sum = {}
    max_length = 0
    current_sum = 0

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the current sum
        current_sum += num
        
        # If the current sum equals zero, update max_length to the current index + 1
        if current_sum == 0:
            max_length = i + 1
        else:
            # If the current sum is already present in the prefix_sum dictionary,
            # update max_length with the maximum of its current value and the difference
            # between the current index and the index stored in the prefix_sum dictionary
            if current_sum in prefix_sum:
                max_length = max(max_length, i - prefix_sum[current_sum])
            else:
                # If the current sum is not present in the prefix_sum dictionary,
                # store it along with its index
                prefix_sum[current_sum] = i
    
    return max_length

# Main function to test the largest_subarray_with_zero_sum function
if __name__ == "__main__":
    nums = [15, -2, 2, -8, 1, 7, 10, 23]
    max_length = largest_subarray_with_zero_sum(nums)
    
    # Print the length of the largest subarray with zero sum
    print("Largest Subarray With Zero Sum:", max_length)
