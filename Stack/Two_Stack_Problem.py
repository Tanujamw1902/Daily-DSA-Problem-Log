# Two Stack Problem... 

class TwoStack:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.top1 = -1  # Top of stack 1
        self.top2 = size  # Top of stack 2

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = data

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = data

    def pop1(self):
        if self.top1 >= 0:
            ans = self.arr[self.top1]
            self.top1 -= 1
            return ans
        else:
            return -1  # Stack underflow

    def pop2(self):
        if self.top2 < self.size:
            ans = self.arr[self.top2]
            self.top2 += 1
            return ans
        else:
            return -1  # Stack underflow


# Example usage
if __name__ == "__main__":
    ts = TwoStack(10)
    ts.push1(10)
    ts.push2(20)
