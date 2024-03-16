# Reverse A String... 

def reverse_string(s):
    """
    Function to reverse a string in-place.

    Args:
    - s: The input string.

    Returns:
    - None (The string is reversed in-place).
    """
    # Convert string to a list of characters for in-place swapping
    s_list = list(s)
    low = 0
    high = len(s) - 1

    while low < high:
        # Swap characters at low and high positions
        s_list[low], s_list[high] = s_list[high], s_list[low]
        low += 1
        high -= 1
    
    # Convert the list of characters back to a string
    s = ''.join(s_list)
    return s

# Main function to test the reverse_string function
if __name__ == "__main__":
    s = "Tanuja"
    reversed_str = reverse_string(s)
    print(reversed_str)
