# 6. Write a program to implement Heap data structure in python.

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] <= self.heap[i]:
                break
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        i = 0
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

        return root


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] >= self.heap[i]:
                break
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        i = 0
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

        return root


if __name__ == "__main__":
    values = [35, 10, 25, 5, 20, 15, 30]

    min_heap = MinHeap()
    for v in values:
        min_heap.insert(v)
    print("Min heap:", min_heap.heap)
    print("Min extract order:")
    while len(min_heap.heap) > 0:
        print(min_heap.extract_min(), end=" ")

    print("\n")

    max_heap = MaxHeap()
    for v in values:
        max_heap.insert(v)
    print("Max heap:", max_heap.heap)
    print("Max extract order:")
    while len(max_heap.heap) > 0:
        print(max_heap.extract_max(), end=" ")
    print()
