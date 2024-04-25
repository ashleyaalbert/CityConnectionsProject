class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            return True
        return False

def kruskal(graph, num_nodes):
    # Collect all unique edges
    edges = set()
    total_weight = 0
    for start, connections in graph.items():
        for id, _, end, weight in connections:
            if start < end:
                edges.add((id, start, end, weight))
    
    # Convert to list and sort by weight
    edges = list(edges)
    edges.sort(key=lambda x: x[3])

    uf = UnionFind(num_nodes)
    mst = []  # To store the result

    for id, start, end, weight in edges:
        if uf.union(start, end):
            total_weight += weight
            mst.append((id, start, end, weight))
            if len(mst) == num_nodes - 1:
                break

    return total_weight, mst

