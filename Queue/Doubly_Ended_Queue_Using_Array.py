# Doubly Ended Queue Using Array... 

class Deque:
    def __init__(self, size):
        self.capacity = size  # Maximum size of the deque
        self.arr = [None] * self.capacity  # Array to hold deque elements
        self.front = -1  # Initialize front pointer
        self.rear = -1  # Initialize rear pointer

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def get_front(self):
        if self.is_empty():
            return -1
        else:
            return self.arr[self.front]

    def get_rear(self):
        if self.is_empty():
            return -1
        else:
            return self.arr[self.rear]

    def push_front(self, x):
        if self.is_full():
            print("Deque overflow")
            return False
        else:
            if self.front == -1:  # Handle circular condition for front
                self.rear = 0
            self.front = (self.front - 1 + self.capacity) % self.capacity
            self.arr[self.front] = x
            return True

    def push_rear(self, x):
        if self.is_full():
            print("Deque overflow")
            return False
        else:
            if self.rear == self.capacity - 1 and self.front == -1:  # Handle circular condition for rear
                self.front = 0
            self.rear = (self.rear + 1) % self.capacity
            self.arr[self.rear] = x
            return True

    def pop_front(self):
        if self.is_empty():
            print("Deque underflow")
            return -1
        else:
            x = self.arr[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity  # Handle circular condition for front
            return x

    def pop_rear(self):
        if self.is_empty():
            print("Deque underflow")
            return -1
        else:
            x = self.arr[self.rear]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.rear = (self.rear - 1 + self.capacity) % self.capacity  # Handle circular condition for rear
            return x

# Main function
if __name__ == "__main__":
    deque = Deque(5)  # Create a deque of size 5

    print("Initial deque:", end=" ")
    for i in range(deque.front, deque.rear):
        print(deque.arr[i], end=" ")
    print()

    deque.push_front(10)
    deque.push_rear(20)
    deque.push_front(5)
    print("Deque after insertions:", end=" ")
    for i in range(deque.front, deque.rear):
        print(deque.arr[i], end=" ")
    print()

    print("Front element:", deque.get_front())
    print("Rear element:", deque.get_rear())

    deque.pop_front()
    deque.pop_rear()
    print("Deque after deletions:", end=" ")
    for i in range(deque.front, deque.rear):
        print(deque.arr[i], end=" ")
    print()
