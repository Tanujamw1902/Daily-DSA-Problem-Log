# Check If ith Bit Is Set Or Not... 

def check_ith_bit(n, i):
    # Approach 1
    # if (n & (1 << i)) != 0:
    #     return "Bit Is Set"
    # else:
    #     return "Bit Is Not Set"

    # Approach 2
    if (n >> i) & 1 == 0:
        return "Bit Is Not Set"
    else:
        return "Bit Is Set"

if __name__ == "__main__":
    n = int(input("Enter Number: "))
    i = int(input("Enter i Value: "))
    result = check_ith_bit(n, i)
    print(result)
