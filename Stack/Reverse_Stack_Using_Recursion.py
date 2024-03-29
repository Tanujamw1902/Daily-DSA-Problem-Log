# Reverse Stack Using Recursion... 

def insert_at_bottom(stack, x):
    if not stack:
        stack.append(x)
        return

    num = stack.pop()
    insert_at_bottom(stack, x)
    stack.append(num)


def reverse_stack(stack):
    if not stack:
        return

    num = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, num)


if __name__ == "__main__":
    stack = [1, 2, 3]
    reverse_stack(stack)

    while stack:
        num = stack.pop()
        print(num, end=" ")

