# Count And Say... 

def count_and_say(n):
    """
    Function to generate the count-and-say sequence up to the nth term.

    Args:
    - n: The number of terms to generate.

    Returns:
    - The nth term of the count-and-say sequence.
    """
    if n == 1:
        return "1"
    if n == 2:
        return "11"

    s = "11"
    for _ in range(3, n + 1):
        t = ""
        s += "&"  # Adding a delimiter to simplify the counting process
        count = 1
        for j in range(1, len(s)):
            # If the current character is different from the previous one,
            # append the count of the previous character and the character itself to the new string
            if s[j] != s[j - 1]:
                t += str(count)
                t += s[j - 1]
                count = 1
            else:
                # If the current character is the same as the previous one, increment the count
                count += 1
        s = t

    return s

# Main function to test the count_and_say function
if __name__ == "__main__":
    n = 5
    print(count_and_say(n))
