# Queue Implementation... 

from queue import Queue

if __name__ == "__main__":
    q = Queue()  # Create a queue

    # Enqueue elements
    q.put(10)
    q.put(20)
    q.put(30)
    q.put(40)
    q.put(50)

    # Dequeue elements and print front element
    print("Queue Out:", q.queue[0])
    q.get()
    print("Queue Out:", q.queue[0])
    q.get()
    print("Queue Out:", q.queue[0])
    q.get()
    print("Queue Out:", q.queue[0])
    q.get()
    print("Queue Out:", q.queue[0])
    q.get()

    # Print size of the queue
    print("Size Of Queue:", q.qsize())

    # Check if queue is empty
    if q.empty():
        print("Queue Is Empty")
    else:
        print("Queue Is Not Empty")
