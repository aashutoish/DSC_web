#1. Write a program to implement stack from scratch in python using array.
class ArrayStack:
    def __init__(self, size):
        self.capacity = size   # changed name
        self.top = -1
        self.stack = [None] * size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, x):
        if self.is_full():
            raise Exception('Stack Overflow: Cannot push element')
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.is_empty():
            raise Exception('Stack Underflow: Cannot pop element')
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception('Stack Underflow: Cannot access element')
        return self.stack[self.top]

    def get_size(self):
        return self.top + 1

if __name__ == "__main__":
    s = ArrayStack(3)

    s.push(10)
    s.push(20)
    s.push(30)

    print(s.pop())   # 30
    print(s.peek())  # 20
    print(s.get_size())  # 2
