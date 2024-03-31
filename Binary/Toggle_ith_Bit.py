# Toggle The ith Bit... 

def toggle_ith_bit(n, i):
    print("Before toggling the ith bit:", bin(n))

    n = n ^ (1 << i)  # Toggle the ith bit

    print("After toggling the ith bit:", bin(n))

if __name__ == "__main__":
    n = int(input("Enter Number: "))
    i = int(input("Enter i Value: "))
    toggle_ith_bit(n, i)
