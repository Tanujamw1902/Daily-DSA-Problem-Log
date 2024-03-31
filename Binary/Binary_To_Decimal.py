# Binary To Decimal Implementation... 

def convert_to_decimal(binary):
    length = len(binary)
    power_of_two = 1
    num = 0

    for i in range(length - 1, -1, -1):
        if binary[i] == '1':
            num += power_of_two
        power_of_two *= 2

    return num

if __name__ == "__main__":
    binary = input("Enter Binary Number: ")
    decimal = convert_to_decimal(binary)
    print("Decimal Representation:", decimal)
