# 3. Write a program for Bracket Matching using using above created Stack. 
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

def is_balanced(expression):
    stack = Stack()
    bracket_map = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in bracket_map.values():
            stack.push(char)
        
        elif char in bracket_map:
            if not stack or stack.peek() != bracket_map[char]:
                return False
            stack.pop()
    return stack.size() == 0


if __name__=="__main__":
    print("--- Balanced Brackets Check ---")
    expr1 = "{[()]()}"
    expr2 = "{[(])}"
    print(f"'{expr1}' is balanced: {is_balanced(expr1)}")
    print(f"'{expr2}' is balanced: {is_balanced(expr2)}")
