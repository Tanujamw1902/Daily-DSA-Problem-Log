# Reverse First K Elements... 

from queue import LifoQueue, Queue


def reverse_first_k(q, k):
    # Create a stack to store the first k elements
    s = LifoQueue()
    for _ in range(k):
        val = q.queue[0]
        q.get()
        s.put(val)

    # Push the elements from the stack back into the queue
    while not s.empty():
        val = s.queue[-1]
        s.get()
        q.put(val)

    # Rotate the remaining elements to maintain the order
    for _ in range(q.qsize() - k):
        val = q.queue[0]
        q.get()
        q.put(val)

    # Print the modified queue
    while not q.empty():
        print(q.queue[0])
        q.get()

if __name__ == "__main__":
    q = Queue()
    q.put(10)
    q.put(20)
    q.put(30)
    q.put(40)
    q.put(50)
    k = 5
    reverse_first_k(q, k)
