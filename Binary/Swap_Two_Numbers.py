# Swap Two Numbers Without Using Third Variable... 

def swap_without_third_var(a, b):
    print("Before Swapping:")
    print("First Value :", a)
    print("Second Value :", b)

    a = a ^ b
    b = a ^ b
    a = a ^ b

    print("\nAfter Swapping:")
    print("First Value :", a)
    print("Second Value :", b)

if __name__ == "__main__":
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    swap_without_third_var(a, b)
