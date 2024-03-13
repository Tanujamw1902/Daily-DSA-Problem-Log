# Program for First Repeated Character...

def first_repeated_char(s):
    char_count = {}
    for ch in s:
        if ch in char_count:
            return ch
        else:
            char_count[ch] = 1
    return "-1"

# Example usage:
str1 = "Tanuja"
print(first_repeated_char(str1))
