# Program to perform the Tower of Hanoi... 

# Function to solve Tower of Hanoi problem
def toh(n, from_rod, to_rod, aux_rod):
    # Base Case: If there are no disks to move, return
    if n == 0:
        return
    
    # Move n-1 disks from the source rod to the auxiliary rod
    toh(n - 1, from_rod, aux_rod, to_rod)
    
    # Move the nth disk from the source rod to the destination rod
    print("Move Disk", n, "From Rod", from_rod, "To Rod", to_rod)
    
    # Move the n-1 disks from the auxiliary rod to the destination rod
    toh(n - 1, aux_rod, to_rod, from_rod)

# Main function
def main():
    n = 3  # Define the number of disks
    toh(n, 'A', 'C', 'B')  # Call the toh function with initial configurations

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
