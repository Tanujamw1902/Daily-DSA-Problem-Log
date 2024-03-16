# Implement strStr()... 

def str_str(haystack, needle):
    """
    Function to find the index of the first occurrence of needle in haystack.

    Args:
    - haystack: The input string to search in.
    - needle: The substring to search for.

    Returns:
    - The index of the first occurrence of needle in haystack, or -1 if needle is not found.
    """
    if not needle:
        return 0
    
    m, n = len(haystack), len(needle)
    
    for i in range(m - n + 1):
        for j in range(n):
            if haystack[i + j] != needle[j]:
                break
        else:
            return i
    
    return -1

# Main function to test the str_str function
if __name__ == "__main__":
    haystack = "Hello"
    needle = "lo"
    print(str_str(haystack, needle))
