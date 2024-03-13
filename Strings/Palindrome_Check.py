# Program to check Palindrome String...

def check_palindrome(s):
    low = 0
    high = len(s) - 1
    while low < high:
        # if 1st and last characters are not equal then return False
        if s[low] != s[high]:
            return False
        # otherwise, move low pointer to the right and high pointer to the left
        low += 1
        high -= 1
    return True

# Example usage:
string = "BOB"
if check_palindrome(string):
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")
