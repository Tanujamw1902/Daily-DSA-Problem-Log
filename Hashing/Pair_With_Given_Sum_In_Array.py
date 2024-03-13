# Check if pair with given Sum exists in an Array(Two Sum)...

def printPairs(arr, n, target_sum):
    # Create a set to store elements as we iterate through the array
    seen = set()

    for num in arr:
        # Calculate the complement needed to achieve the target sum
        complement = target_sum - num
        
        # If the complement exists in the set, then a pair exists
        if complement in seen:
            print("Yes")
            return
        
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If no pair is found after iterating through the array
    print("No")

# Main function
if __name__ == "__main__":
    arr = [1, 2, 5, 3, 6, 8]
    target_sum = 8
    printPairs(arr, len(arr), target_sum)
