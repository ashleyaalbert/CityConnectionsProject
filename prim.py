def prim_mst(graph):
    V = len(graph)
    selected = [False] * V
    selected[0] = True
    no_edge = 0
    total_weight = 0
    tree_edges = []
    while no_edge < V - 1:
        minimum = 9999999
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j].weight:
                        if minimum > graph[i][j].weight:
                            minimum = graph[i][j].weight
                            x = i
                            y = j
        tree_edges.append((graph[x][y].id, graph[y][x].id))
        total_weight += graph[x][y].weight
        selected[y] = True
        no_edge += 1
    return total_weight, tree_edges