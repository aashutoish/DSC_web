# 7. Write a program in python to implement Priority Queue data structure using array.
class Node:
  def __init__(self, info, priority):
    self.info = info
    self.priority = priority

class PriorityQueue:
  def __init__(self):
    self.queue = []

  def insert(self, info, priority):
    node = Node(info, priority)
    
    if len(self.queue) == 0:
      self.queue.append(node)
    else:
      inserted = False
      for i in range(len(self.queue)):
        if node.priority < self.queue[i].priority:
          self.queue.insert(i, node)
          inserted = True
          break
      
      if not inserted:
        self.queue.append(node)

  def delete(self):
    if len(self.queue) == 0:
      return None
    else:
      return self.queue.pop(0)

  def display(self):
    for node in self.queue:
      print(f"Info: {node.info}, Priority: {node.priority}")

if __name__ == "__main__":
  pq = PriorityQueue()
  
  pq.insert("Task A", 3)
  pq.insert("Task B", 1)
  pq.insert("Task C", 2)
  
  print("Priority Queue:")
  pq.display()
  
  deleted = pq.delete()
  if deleted:
    print("\nDeleted:", deleted.info)
  
  print("\nPriority Queue after deletion:")
  pq.display()
