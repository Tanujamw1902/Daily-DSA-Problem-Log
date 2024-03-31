# Count Set Of Bits... 

def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter Number: "))
    set_bits_count = count_set_bits(n)
    print("Count of set bits:", set_bits_count)
