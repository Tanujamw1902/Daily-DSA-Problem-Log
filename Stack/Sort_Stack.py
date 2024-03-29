# Sort Stack... 

def sort_inserted(stack, num):
    if not stack or stack[-1] < num:
        stack.append(num)
        return

    n = stack.pop()
    sort_inserted(stack, num)
    stack.append(n)

def sort_stack(stack):
    # Base Case
    if not stack:
        return

    num = stack.pop()

    sort_stack(stack)

    sort_inserted(stack, num)

if __name__ == "__main__":
    stack = [5, 4, 3, 2, 1]

    # Sort the stack
    sort_stack(stack)

    # Print the sorted stack
    while stack:
        num = stack.pop()
        print(num, end=" ")


