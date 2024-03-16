# Longest Substring Without Repeating Characters... 

def longest_substring(s):
    """
    Function to find the length of the longest substring without repeating characters.

    Args:
    - s: The input string.

    Returns:
    - The length of the longest substring without repeating characters.
    """
    char_set = set()
    left = 0
    right = 0
    max_length = 0

    while right < len(s):
        if s[right] not in char_set:
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            char_set.remove(s[left])
            left += 1

    return max_length

# Main function to test the longest_substring function
if __name__ == "__main__":
    s = "asbdjdsaaasndjaasdan"
    print(longest_substring(s))
