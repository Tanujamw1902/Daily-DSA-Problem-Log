# Valid Parenthesis... 

def valid(s):
    """
    Function to check if the given string of parentheses is valid.

    Args:
    - s: The input string containing parentheses.

    Returns:
    - True if the parentheses are valid, False otherwise.
    """
    stack = []

    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if not stack or (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{'):
                return False
            stack.pop()

    return not stack

# Main function to test the valid function
if __name__ == "__main__":
    s = "()(){}[][]"
    print(valid(s))
