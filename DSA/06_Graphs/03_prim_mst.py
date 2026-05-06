# 3. Prim's Algorithm for Minimum Spanning Tree

import heapq

class PrimMST:
    def __init__(self):
        self.g = {}

    def add_edge(self, u, v, weight):
        if u not in self.g:
            self.g[u] = []
        if v not in self.g:
            self.g[v] = []
        self.g[u].append((weight, v))
        self.g[v].append((weight, u))

    def prim(self, start=None):
        if not self.g:
            return [], 0

        if start is None:
            start = next(iter(self.g))

        visited = set()
        ans = []
        total = 0

        heap = [(0, start, None)]

        while heap and len(visited) < len(self.g):
            w, node, parent = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            if parent is not None:
                ans.append((parent, node, w))
                total += w

            for next_w, nei in self.g[node]:
                if nei not in visited:
                    heapq.heappush(heap, (next_w, nei, node))

        return ans, total

    def find_mst(self, start=None):
        return self.prim(start)

if __name__ == "__main__":
    prim = PrimMST()

    edges = [
        ("A", "B", 4), ("A", "C", 2), ("B", "C", 1),
        ("B", "D", 5), ("C", "D", 8), ("C", "E", 10),
        ("D", "E", 2), ("D", "F", 6), ("E", "F", 3),
    ]
    for u, v, w in edges:
        prim.add_edge(u, v, w)

    mst_edges, total = prim.prim("A")

    print("MST:")
    for u, v, w in mst_edges:
        print(u, v, w)
    print("Total:", total)

    # Numbered example
    prim2 = PrimMST()
    edges2 = [
        (0, 1, 10), (0, 2, 6), (0, 3, 5),
        (1, 3, 15), (2, 3, 4),
    ]
    for u, v, w in edges2:
        prim2.add_edge(u, v, w)

    mst2, total2 = prim2.prim(0)
    print("\nMST2:", mst2)
    print("Total2:", total2)
