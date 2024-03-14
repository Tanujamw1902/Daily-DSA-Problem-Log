# Program to perform for Subsets of Set using Recursion... 

# Function to generate subsets of a set
def subsets(string, index=0, curr=""):
    n = len(string)
    # Base Case: If index reaches the length of the string, return
    if index == n:
        return
    print(curr)  # Print the current subset

    # Recursive call to generate subsets with each character included
    for i in range(index + 1, n):
        curr += string[i]
        subsets(string, i, curr)
        curr = curr[:-1]  # Backtrack by removing the last character

# Main function
def main():
    string = "abc"  # Define the string for which subsets will be generated
    subsets(string)  # Call the subsets function with the string

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
