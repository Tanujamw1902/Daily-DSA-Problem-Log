# Finding the First Occurence of Character in a String... 

def find_element(string, ch):
    """
    Function to find the index of the first occurrence of a character in a string.

    Args:
    - string: The input string.
    - ch: The character to search for.

    Returns:
    - The index of the first occurrence of the character if found, otherwise -1.
    """
    # Iterate through each character in the string
    for i in range(len(string)):
        # Check if the current character matches the target character
        if string[i] == ch:
            # Return the index of the first occurrence of the character
            return i
    
    # If the character is not found, return -1
    return -1

# Main function to test the find_element function
if __name__ == "__main__":
    # Input string
    string = "hello world"
    # Character to search for
    ch = 'o'
    
    # Call the find_element function and print the result
    print(find_element(string, ch))
