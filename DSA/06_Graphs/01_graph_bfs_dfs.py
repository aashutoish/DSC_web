# 1. Graph Traversal using BFS and DFS

from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))

    def bfs(self, start):
        visited = set()
        order = []
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor, _ in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        visited = set()
        order = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor, _ in reversed(self.adj_list.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def dfs_recursive(self, start, visited=None, order=None):
        if visited is None:
            visited = set()
        if order is None:
            order = []
        visited.add(start)
        order.append(start)
        for neighbor, _ in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, order)
        return order

if __name__ == "__main__":
    g = Graph(directed=False)

    edges = [
        ("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"),
        ("C", "F"), ("D", "G"), ("E", "G"), ("F", "G"),
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print("BFS from A:", g.bfs("A"))
    print("DFS from A:", g.dfs("A"))
    print("DFS Recursive from A:", g.dfs_recursive("A"))

    # Numbered graph
    g2 = Graph(directed=False)
    edges2 = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (2, 6), (3, 7), (4, 7),
    ]
    for u, v in edges2:
        g2.add_edge(u, v)

    print("\nBFS from 0:", g2.bfs(0))
    print("DFS from 0:", g2.dfs(0))
