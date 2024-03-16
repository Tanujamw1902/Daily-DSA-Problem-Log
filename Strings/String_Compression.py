# String Compression... 

def scomp(s):
    """
    Function to perform string compression by counting consecutive characters.

    Args:
    - s: The input string.

    Returns:
    - The compressed string if it is shorter than the original string, otherwise the original string.
    """
    compression = ""
    count = 1
    n = len(s)
    
    for i in range(n):
        # Check if the current character is the same as the next one
        if i + 1 < n and s[i] == s[i + 1]:
            count += 1
        else:
            # If the next character is different or it's the end of the string,
            # append the current character and its count to the compression string
            compression += s[i] + str(count)
            count = 1
    
    # Check if the compressed string is shorter than the original string
    return compression if len(compression) < len(s) else s

# Main function to test the scomp function
if __name__ == "__main__":
    s = "aaaabbbcccc"
    print(scomp(s))
