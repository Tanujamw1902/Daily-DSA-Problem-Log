# Set ith Bit... 

def set_ith_bit(n, i):
    result = n | (1 << i)  # Set the ith bit
    return result

if __name__ == "__main__":
    n = int(input("Enter Number: "))
    i = int(input("Enter i Value: "))
    result = set_ith_bit(n, i)
    print("Bit Settled:", result)
