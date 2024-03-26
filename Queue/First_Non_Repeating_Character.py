# First Non Repeating Character... 

from collections import defaultdict, deque


def first_non_repeating(A):
    count = defaultdict(int)  # Dictionary to store the count of characters
    q = deque()  # Queue to store characters in the order they appear

    for ch in A:
        count[ch] += 1  # Increment count of character
        q.append(ch)  # Add character to the queue

        # Remove characters from the queue until finding the first non-repeating character
        while q and count[q[0]] > 1:
            q.popleft()

    if q:
        return q[0]  # Return the first non-repeating character
    else:
        return '#'  # If no non-repeating character found

# Main function
if __name__ == "__main__":
    A = "aabc"
    first_non_repeating_char = first_non_repeating(A)
    if first_non_repeating_char != '#':
        print(first_non_repeating_char)
    else:
        print("No non-repeating character found.")
