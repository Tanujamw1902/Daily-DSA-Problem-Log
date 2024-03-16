# String To Integer(atoi)... 

def str_to_int(s):
    """
    Function to convert a string to an integer.

    Args:
    - s: The input string containing the integer.

    Returns:
    - The converted integer value.
    """
    i = 0
    sign = 1
    result = 0

    # Skip leading whitespace
    while i < len(s) and s[i] == ' ':
        i += 1

    # Handle sign
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Process digits
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit
        i += 1

    return result * sign

# Main function to test the str_to_int function
if __name__ == "__main__":
    s = "2004"
    print(str_to_int(s))
