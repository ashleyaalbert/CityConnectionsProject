class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size)) # Initially, each node is its own parent
        self.rank = [0] * size # Rank of each node

    def find(self, p):
        # This function recursively finds the root of the element 'p'
        # while making the elements along the path point directly to the root.
        # This is done to reduce the height of the tree.
        if self.parent[p] != p: # If p is not its own parent keep recursing until it is
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        # Union by rank this function connects the roots of the trees containing 'p' and 'q'
        # It attaches the tree with lower rank under the root of the higher rank tree.
        # If ranks are the same, it arbitrarily chooses one as root and increases its rank by 1.
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:  # Only unite if 'p' and 'q' are in different sets
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            return True # Indicates that a union was performed
        return False # No union preformed

def kruskal(graph, num_nodes):
    # Prepare to collect all unique edges from the adjacency list to form a set (no duplicates).
    # The graph is represented as a dictionary where each key is a node and each value is a list of connections.
    # Each connection is a tuple containing the edge ID, another start, end, and the weight of the edge.
    edges = set()
    total_weight = 0
    # Extract edges ensuring each edge is only considered once (e.g., only (start, end) not (end, start))
    for start, connections in graph.items():
        for id, _, end, weight in connections:
            if start < end:
                edges.add((id, start, end, weight))
    
    # Sort all edges by weight in ascending order to prepare for the MST creation
    edges = list(edges)
    edges.sort(key=lambda x: x[3]) #sorting based on the fouth element of the tuple (weight)

    uf = UnionFind(num_nodes) # Initialize the Union-Find structure for the number of nodes
    mst = []  # will hold edges of the minimum spanning tree

    for id, start, end, weight in edges: 
        # For each edge, use union to attempt to add it to the MST
        if uf.union(start, end): # If the edge was added to the MST
            total_weight += weight # Add the weight of the edge to the total weight of the MST
            mst.append((id, start, end, weight)) # Add this edge to the MST
            if len(mst) == num_nodes - 1: # If the MST has same number of edges as nodes - 1 we are done
                break

    return total_weight, mst

