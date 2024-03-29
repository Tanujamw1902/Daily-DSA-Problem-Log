# Redundant Brackets... 

def is_redundant(s):
    stack = []
    for ch in s:
        if ch in '()+-*/':
            stack.append(ch)
        else:
            if ch == ')':
                redundant = True
                while stack[-1] != '(':
                    top = stack.pop()
                    if top in '()+-*/':
                        redundant = False
                stack.pop()  # Remove '('
                if redundant:
                    return True
    return False

if __name__ == "__main__":
    s = "((a+b))"
    print(is_redundant(s))

