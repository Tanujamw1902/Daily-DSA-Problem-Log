# Clear The ith Bit... 

def clear_ith_bit(n, i):
    return n & ~(1 << i)

if __name__ == "__main__":
    n = int(input("Enter Number: "))
    i = int(input("Enter i Value: "))
    
    cleared_number = clear_ith_bit(n, i)
    print("Number after clearing the ith bit:", cleared_number)
