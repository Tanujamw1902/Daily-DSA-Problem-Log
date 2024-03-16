# Group Anagrams... 

def group_anagrams(strs):
    """
    Function to group anagrams together from a list of strings.

    Args:
    - strs: A list of strings.

    Returns:
    - A list of lists containing groups of anagrams.
    """
    # Initialize a dictionary to store groups of anagrams
    groups = {}

    # Iterate through each string in the input list
    for s in strs:
        # Sort the characters of the string to form a key
        key = ''.join(sorted(s))
        
        # If the key (sorted string) exists in the dictionary, append the string to its corresponding group
        if key in groups:
            groups[key].append(s)
        # Otherwise, create a new entry in the dictionary with the key and the string as its value
        else:
            groups[key] = [s]
    
    # Convert the dictionary values (lists of anagrams) to a list of lists
    result = list(groups.values())

    return result

# Main function to test the group_anagrams function
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    for group in result:
        print(' '.join(group))
