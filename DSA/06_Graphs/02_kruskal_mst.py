# 2. Kruskal's Algorithm for Minimum Spanning Tree

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

class KruskalMST:
    def __init__(self):
        self.edges = []
        self.vertices = set()

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))
        self.vertices.add(u)
        self.vertices.add(v)

    def find_mst(self):
        self.edges.sort()
        ds = DisjointSet(self.vertices)

        mst_edges = []
        total_weight = 0

        for weight, u, v in self.edges:
            if ds.union(u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight

            if len(mst_edges) == len(self.vertices) - 1:
                break

        return mst_edges, total_weight

if __name__ == "__main__":
    kruskal = KruskalMST()

    edges = [
        ("A", "B", 4), ("A", "C", 2), ("B", "C", 1),
        ("B", "D", 5), ("C", "D", 8), ("C", "E", 10),
        ("D", "E", 2), ("D", "F", 6), ("E", "F", 3),
    ]
    for u, v, w in edges:
        kruskal.add_edge(u, v, w)

    mst_edges, total = kruskal.find_mst()

    print("MST Edges:")
    for u, v, w in mst_edges:
        print(f"  {u} - {v} (weight: {w})")
    print(f"Total MST Weight: {total}")

    # Numbered example
    kruskal2 = KruskalMST()
    edges2 = [
        (0, 1, 10), (0, 2, 6), (0, 3, 5),
        (1, 3, 15), (2, 3, 4),
    ]
    for u, v, w in edges2:
        kruskal2.add_edge(u, v, w)

    mst2, total2 = kruskal2.find_mst()
    print(f"\nMST Edges: {[(u, v, w) for u, v, w in mst2]}")
    print(f"Total MST Weight: {total2}")
