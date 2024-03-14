# Program for Indirect Recursion...

# Function to demonstrate indirect recursion
def function_A(n):
    if n > 0:
        print("", n, end='')  # Print the current value of n

        # Call function_B
        function_B(n - 1)  # Call function_B with n - 1 as the argument

def function_B(n):
    if n > 1:
        print("", n, end='')  # Print the current value of n

        # Call function_A
        function_A(n // 2)  # Call function_A with n // 2 as the argument

# Execution starts here
function_A(20)  # Call function_A with 20
