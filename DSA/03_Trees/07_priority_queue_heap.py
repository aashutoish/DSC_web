# 7. Write a program to implement priority queue using heap data structure in python
class PriorityQueueHeap:
    def __init__(self):
        self.heap = [(0, "")]  # type: list[tuple[int, str]]
        self.size = 0

    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k][0] < self.heap[k//2][0]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, priority, item):
        self.heap.append((priority, item))
        self.size += 1
        self.arrange(self.size)

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.minchild(k)
            if self.heap[k][0] > self.heap[mc][0]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def minchild(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2][0] < self.heap[k*2+1][0]:
            return k * 2
        else:
            return k * 2 + 1

    def delete_at_root(self):
        item = self.heap[1][1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

if __name__ == "__main__":
    h = PriorityQueueHeap() 
    h.insert(2, "Bat") 
    h.insert(13, "Cat")
    h.insert(18, "Rat")
    h.insert(26, "Ant")
    h.insert(3, "Lion")
    h.insert(4, "Bear")

    for i in range(h.size):
        n = h.delete_at_root()
        print(n)
        print("Heap:", h.heap)
