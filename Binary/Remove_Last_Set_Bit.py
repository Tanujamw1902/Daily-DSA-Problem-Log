# Remove The LastSet Bit --> Rightmost... 

def remove_rightmost_set_bit(n):
    result = n & (n - 1)  # Remove the rightmost set bit
    return result

if __name__ == "__main__":
    n = int(input("Enter Number: "))
    result = remove_rightmost_set_bit(n)
    print("Number with the rightmost set bit removed:", result)
