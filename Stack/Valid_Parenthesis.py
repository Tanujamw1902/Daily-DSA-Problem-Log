# Valid Parenthesis... 

def is_valid_parenthesis(expression):
    stack = []

    for ch in expression:
        if ch in ['(', '[', '{']:
            stack.append(ch)
        else:
            if stack:
                top = stack[-1]
                if (ch == ')' and top == '(') or (ch == ']' and top == '[') or (ch == '}' and top == '{'):
                    stack.pop()
                else:
                    return False
            else:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    expression = "[{()}]"
    print(is_valid_parenthesis(expression))
