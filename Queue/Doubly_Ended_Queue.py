# Doubly Ended Queue... 

from collections import deque

if __name__ == "__main__":
    d = deque()  # Create a deque

    # Insert elements at the front
    d.appendleft(12)
    d.appendleft(22)
    d.appendleft(32)
    d.appendleft(42)
    d.appendleft(52)

    # Insert elements at the rear
    d.append(52)
    d.append(42)
    d.append(32)
    d.append(22)
    d.append(12)

    d.popleft()  # Remove an element from the front
    print(d[0])  # Print the front element
    print(d[-1])  # Print the rear element

    if not d:  # Check if the deque is empty
        print("Queue Is Empty")
    else:
        print("Queue Is Not Empty")
