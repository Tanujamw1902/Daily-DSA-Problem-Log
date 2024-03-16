# Anagram Detection... 

def is_anagram(s1, s2):
    """
    Function to check if two strings are anagrams of each other.

    Args:
    - s1: The first string.
    - s2: The second string.

    Returns:
    - True if the strings are anagrams, False otherwise.
    """
    # If the lengths of the strings are not equal, they cannot be anagrams
    if len(s1) != len(s2):
        return False
    
    # Initialize a dictionary to store the frequency of characters in s1
    char_freq = {}
    
    # Count the frequency of characters in s1
    for char in s1:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Check if the characters in s2 have the same frequencies as in s1
    for char in s2:
        if char not in char_freq or char_freq[char] == 0:
            return False
        char_freq[char] -= 1
    
    return True

# Main function to test the is_anagram function
if __name__ == "__main__":
    s1 = "anagram"
    s2 = "nagaram"
    print(is_anagram(s1, s2))
