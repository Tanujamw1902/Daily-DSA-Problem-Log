# Reverse String Using Stack... 

def reverse_string(input_str):
    stack = []

    # Push each character of the input string onto the stack
    for ch in input_str:
        stack.append(ch)

    reversed_str = ""

    # Pop each character from the stack and append it to the reversed string
    while stack:
        ch = stack.pop()
        reversed_str += ch

    return reversed_str

if __name__ == "__main__":
    input_str = "Raj"
    reversed_str = reverse_string(input_str)
    print("Reverse String Is:", reversed_str)
