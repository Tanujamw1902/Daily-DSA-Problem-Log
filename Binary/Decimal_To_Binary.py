# Decimal To Binary Implementation... 

def convert_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n != 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

if __name__ == "__main__":
    n = int(input("Enter Number: "))
    binary_representation = convert_to_binary(n)
    print("Binary Representation:", binary_representation)
