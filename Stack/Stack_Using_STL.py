# Stack Using STL... 

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None  # Return None or raise an exception for empty stack

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None  # Return None or raise an exception for empty stack

    def empty(self):
        return len(self.stack) == 0

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    print(s.top())
    s.push(20)
    print(s.top())
    s.push(30)
    print(s.top())
    s.push(40)
    print(s.top())
    s.push(50)
    print(s.top())

    s.pop()
    s.pop()
    s.pop()

    print(s.top())

    if s.empty():
        print("Stack Is Empty !!!")
    else:
        print("Stack Is Not Empty !")
