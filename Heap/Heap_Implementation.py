# Heap Implementation... 

class Heap:
    def __init__(self):
        self.arr = [None] * 100  # Array to store heap elements
        self.size = 0  # Current size of the heap

    # Insertion function
    def insert(self, val):
        self.size += 1
        index = self.size
        self.arr[index] = val
        while index > 1:
            parent = index // 2
            if self.arr[parent] < self.arr[index]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                return

    # Deletion function
    def delete_heap(self):
        if self.size == 0:
            print("Nothing to delete")
            return
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        i = 1
        while i <= self.size:
            left_index = 2 * i
            right_index = 2 * i + 1

            if left_index <= self.size and self.arr[i] < self.arr[left_index]:
                self.arr[i], self.arr[left_index] = self.arr[left_index], self.arr[i]
                i = left_index
            elif right_index <= self.size and self.arr[i] < self.arr[right_index]:
                self.arr[i], self.arr[right_index] = self.arr[right_index], self.arr[i]
                i = right_index
            else:
                return

    # Function to print the heap array
    def print_array(self):
        print(" ".join(str(self.arr[i]) for i in range(1, self.size + 1)))


if __name__ == "__main__":
    h = Heap()

    # Test insertion
    h.insert(4)
    h.insert(10)
    h.insert(7)
    h.insert(1)
    h.insert(3)
    print("After insertion:", end=" ")
    h.print_array()

    # Test deletion
    h.delete_heap()
    print("After deletion:", end=" ")
    h.print_array()
