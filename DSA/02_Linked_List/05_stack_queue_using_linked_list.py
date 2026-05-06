# 5. Stack and Queue implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # type: Node | None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def is_empty(self):
        return self.top is None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def is_empty(self):
        return self.front is None

if __name__ == "__main__":
    # Stack example
    s = Stack()
    s.push(10)
    s.push(20)
    print("Stack pop:", s.pop())
    
    # Queue example
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print("Queue dequeue:", q.dequeue())
