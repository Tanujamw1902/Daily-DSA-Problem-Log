# Circular Queue Using Array... 

class CircularQueue:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n  # Create an array of size n
        self.front = self.rear = -1  # Initialize front and rear pointers

    def enqueue(self, data):
        if (self.front == 0 and self.rear == self.size - 1) or (self.rear == (self.front - 1) % (self.size - 1)):
            print("Queue Is Full")
        elif self.front == -1:  # If queue is initially empty
            self.front = self.rear = 0
            self.arr[self.front] = data
        elif self.rear == self.size - 1 and self.front != 0:  # If rear is at the end and there's space at the beginning
            self.rear = 0
        else:
            self.rear += 1
        self.arr[self.rear] = data
        return True

    def dequeue(self):
        if self.front == -1:  # If queue is empty
            print("Queue Is Empty")
            return -1

        ans = self.arr[self.front]  # Get the element to dequeue
        self.arr[self.front] = None  # Reset the element to None
        if self.front == self.rear:  # If only one element is in the queue
            self.front = self.rear = -1
        elif self.front == self.size - 1:  # If front is at the end of the queue
            self.front = 0
        else:
            self.front += 1
        return ans


# Testing the CircularQueue class
if __name__ == "__main__":
    q = CircularQueue(100)  # Create a circular queue with size 100

    print(q.enqueue(10))  # Enqueue 10
    print(q.dequeue())  # Dequeue an element
