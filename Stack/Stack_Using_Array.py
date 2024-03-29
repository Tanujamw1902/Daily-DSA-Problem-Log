# Stack Using Array... 

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size  # Initialize array with zeros
        self.top = -1

    def push(self, element):
        if self.top < self.size - 1:
            self.top += 1
            self.arr[self.top] = element
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top >= 0:
            self.top -= 1
        else:
            print("Stack Underflow")

    def peek(self):
        if self.top >= 0:
            return self.arr[self.top]
        else:
            print("Stack Is Empty")
            return -1  # Assuming -1 denotes an empty stack, change it according to your requirement

    def empty(self):
        return self.top == -1

    def __del__(self):
        del self.arr

if __name__ == "__main__":
    st = Stack(5)
    st.push(1)
    st.push(2)
    st.push(3)
    print("Top element:", st.peek())
    st.pop()
    print("Top element after pop:", st.peek())
    print("Is stack empty?", "Yes" if st.empty() else "No")
