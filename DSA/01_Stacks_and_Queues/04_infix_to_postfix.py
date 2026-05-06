# 4. Write a program in python to implement Infix to Postfix conversion using Stack 
# implemented above. 
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

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    output = Stack()
    operator_stack = Stack()

    tokens = expression.split()

    for token in tokens:
        if token.isalnum():
            output.push(token)

        elif token == '(':
            operator_stack.push(token)

        
        elif token == ')':
            while (not operator_stack.isEmpty() and 
                   operator_stack.peek() != '('):
                output.push(operator_stack.pop())
            operator_stack.pop()  

        # If operator
        else:
            while (not operator_stack.isEmpty() and
                   operator_stack.peek() != '(' and
                   precedence.get(operator_stack.peek(), 0) >= precedence.get(token, 0)):
                output.push(operator_stack.pop())

            operator_stack.push(token)

    # Pop remaining operators
    while not operator_stack.isEmpty():
        output.push(operator_stack.pop())

    return " ".join(output.stack)


# Example usage
if __name__ == "__main__":
    infix_expr = "( A + B ) * C - ( D / E )"
    postfix_expr = infix_to_postfix(infix_expr)

    print("Infix  :", infix_expr)
    print("Postfix:", postfix_expr)
