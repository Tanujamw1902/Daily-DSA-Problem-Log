# Program for First Non-Repeated Character...

def first_non_rep_char(s):
    char_count = {}
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    
    for ch in s:
        if char_count[ch] == 1:
            return ch
    return None

# Example usage:
str1 = "Tanuja"
print(first_non_rep_char(str1))
