# Delete Middle Element Using Stack... 

# Function to delete the middle element of the stack
def solve(input_stack, count, size):
    if count == size // 2:
        input_stack.pop()
        return
    num = input_stack[-1]
    input_stack.pop()

    solve(input_stack, count + 1, size)
    input_stack.append(num)

# Function to initiate the deletion of the middle element
def delete_middle(input_stack, N):
    count = 0
    solve(input_stack, count, N)

# Function to print the stack elements recursively
def print_stack(stack):
    if not stack:
        return

    x = stack.pop()
    print(x, end=" ")

    print_stack(stack)

    stack.append(x)

if __name__ == "__main__":
    input_stack = [10, 20, 30, 40, 50]
    delete_middle(input_stack, 5)
    print("Stack after deleting middle element:", end=" ")
    print_stack(input_stack)
