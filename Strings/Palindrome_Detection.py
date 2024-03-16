# Program To Check Palindrome String... 

def check_palindrome(s):
    """
    Function to check if a string is a palindrome.

    Args:
    - s: The input string.

    Returns:
    - True if the string is a palindrome, False otherwise.
    """
    low = 0
    high = len(s) - 1

    while low < high:
        # If the characters at low and high positions are not equal, it's not a palindrome
        if s[low] != s[high]:
            return False
        
        # Move low pointer forward and high pointer backward
        low += 1
        high -= 1

    return True

# Main function to test the check_palindrome function
if __name__ == "__main__":
    s = "NAMAN"
    if check_palindrome(s):
        print(s, "is Palindrome")
    else:
        print(s, "not a Palindrome")
