# Queue Reversal... 

from queue import LifoQueue, Queue


def queue_reversal(q, s):
    # Transfer elements from the queue to the stack
    while not q.empty():
        element = q.queue[0]
        q.get()
        s.put(element)
    
    # Transfer elements from the stack back to the queue
    while not s.empty():
        element = s.queue[-1]
        s.get()
        q.put(element)

def print_queue(q):
    while not q.empty():
        print(q.queue[0], end=" ")
        q.get()

if __name__ == "__main__":
    s = LifoQueue()  # Create a stack
    q = Queue()  # Create a queue

    # Enqueue elements to the queue
    q.put(10)
    q.put(20)
    q.put(30)
    q.put(40)
    q.put(50)

    # Reverse the queue
    queue_reversal(q, s)

    # Print the reversed queue
    print_queue(q)
