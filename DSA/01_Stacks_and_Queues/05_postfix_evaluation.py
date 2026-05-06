# 5. Evaluate postfix expression

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if len(self.stack) == 0:
      return None
    return self.stack.pop()

  def size(self):
    return len(self.stack)


def eval_postfix(expression):
  s = Stack()
  tokens = expression.split()

  for token in tokens:
    if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
      s.push(float(token))
    else:
      if s.size() < 2:
        raise ValueError("Invalid expression")

      b = s.pop()
      a = s.pop()

      if a is None or b is None:
        raise ValueError("Invalid expression")

      if token == '+':
        s.push(a + b)
      elif token == '-':
        s.push(a - b)
      elif token == '*':
        s.push(a * b)
      elif token == '/':
        if b == 0:
          raise ValueError("Cannot divide by zero")
        s.push(a / b)
      else:
        raise ValueError("Invalid operator")

  if s.size() != 1:
    raise ValueError("Invalid expression")

  return s.pop()


if __name__ == "__main__":
  exp1 = "3 4 + 2 *"
  exp2 = "7 3 * 4 +"

  print("Postfix:", exp1)
  print("Result:", eval_postfix(exp1))

  print("Postfix:", exp2)
  print("Result:", eval_postfix(exp2))
