# Insert Element At Bottom Using Stack... 

# Function to insert element x at the bottom of the stack
def insert_at_bottom(stack, x):
    # If the stack is empty, push the element x and return
    if not stack:
        stack.append(x)
        return
    
    # Pop the top element from the stack
    num = stack.pop()

    # Recursively insert element x at the bottom of the stack
    insert_at_bottom(stack, x)
    
    # Push the popped element back onto the stack
    stack.append(num)

# Function to print the stack elements recursively
def print_stack(stack):
    if not stack:
        return

    x = stack.pop()
    print(x, end=" ")

    print_stack(stack)

    stack.append(x)

if __name__ == "__main__":
    # Creating a stack and pushing some elements
    s = [1, 2, 3, 4, 5]
    
    # Element to insert at the bottom of the stack
    x = 0
    
    # Inserting x at the bottom of the stack
    insert_at_bottom(s, x)

    # Printing the stack after inserting x at the bottom
    print("Stack after inserting element at bottom:", end=" ")
    print_stack(s)
