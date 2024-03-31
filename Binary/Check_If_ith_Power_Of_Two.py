# Check If The Number Is A Power Of 2... 

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

if __name__ == "__main__":
    n = int(input("Enter Number: "))
    if is_power_of_two(n):
        print("Number Is Power Of Two")
    else:
        print("Number Is Not Power Of Two")
