# Program for Anagram Check...

def is_anagram(str1, str2):
    # Counting the frequency of characters in the first string
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Cross checking frequency of characters in the second string
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
    
    # Check if all counts are zero
    for count in char_count.values():
        if count != 0:
            return False
    
    return True

def main():
    str1 = "lata"
    str2 = "atal"
    if is_anagram(str1, str2):
        print("These strings are anagrams.")
    else:
        print("These strings are not anagrams.")

if __name__ == "__main__":
    main()
