# Queue Using Array... 

class Queue:
    MAX_SIZE = 10  # Maximum size of the queue

    def __init__(self):
        self.arr = [0] * self.MAX_SIZE
        self.qfront = 0
        self.qrear = 0

    def push(self, d):
        if self.qrear == self.MAX_SIZE:
            print("Queue Is Full")
            return
        self.arr[self.qrear] = d
        self.qrear += 1

    def pop(self):
        if self.qfront == self.qrear:
            print("Queue Is Empty")
            return
        self.qfront += 1

    def is_empty(self):
        return self.qfront == self.qrear

    def front(self):
        if self.qfront == self.qrear:
            return -1  # Indicating queue is empty
        return self.arr[self.qfront]

# Main function
if __name__ == "__main__":
    q = Queue()

    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)
    q.push(50)

    print("Is Queue Empty?", "Yes" if q.is_empty() else "No")

    while not q.is_empty():
        print("Front element:", q.front())
        q.pop()
