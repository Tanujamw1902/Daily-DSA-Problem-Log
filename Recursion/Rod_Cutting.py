# Program to perform the Rod Cutting Problem... 

# Function to find the maximum obtainable value by cutting a rod of length n
def cut_rod(prices, n):
    # Base Case: If the length of the rod is 0, return 0
    if n == 0:
        return 0
    
    max_value = float('-inf')

    # Recursively try all possible cuts and choose the one with maximum value
    for i in range(1, n + 1):
        max_value = max(max_value, prices[i - 1] + cut_rod(prices, n - i))

    return max_value

# Main function
def main():
    prices = [1, 5, 8, 9, 10, 17, 17, 20]  # Prices of different lengths of the rod
    size = len(prices)  # Size of the price array
    max_value = cut_rod(prices, size)  # Calculate the maximum obtainable value
    print(max_value)

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
