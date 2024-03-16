# Program for count subarrays with XOR Ask...

def count_subarrays_with_xor_k(nums, K):
    # Dictionary to store the count of prefix XOR sums
    prefix_xor = {}
    count = 0
    xor_sum = 0

    # Iterate through the list of numbers
    for num in nums:
        # Calculate the XOR sum
        xor_sum ^= num
        
        # If the current XOR sum equals K, increment count
        if xor_sum == K:
            count += 1
        
        # If there exists a prefix XOR sum that, when XORed with the current XOR sum, equals K,
        # add the count of such prefix XOR sums to the overall count
        if xor_sum ^ K in prefix_xor:
            count += prefix_xor[xor_sum ^ K]
        
        # Increment the count of the current XOR sum in the prefix XOR dictionary
        prefix_xor[xor_sum] = prefix_xor.get(xor_sum, 0) + 1
    
    return count

# Main function to test the count_subarrays_with_xor_k function
if __name__ == "__main__":
    nums = [4, 2, 2, 6, 4]
    K = 6
    count = count_subarrays_with_xor_k(nums, K)
    
    # Print the number of subarrays with XOR as K
    print("Number Of Subarrays With Xor As K Is:", count)
