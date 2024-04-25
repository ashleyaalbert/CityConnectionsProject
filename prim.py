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
        for i in range(V): # loop through vertices
            if selected[i]:
                
                # TODO: this could probably be added to the graph's tuple
                # Add edges adjacent to i to a list
                # Store offset value to find adjacent edges' index in the adjacency list to vertex i
                adj_edges = []
                offset_dict = {}
                for edge_index in range(len(graph[i])): 
                    end_vertex = graph[i][edge_index][2]
                    offset_dict[end_vertex] = edge_index - end_vertex # end_vertex + offset = index in adjacency list for vertex i
                    adj_edges.append(end_vertex)

                for j in adj_edges: # loop through adjacent edges
                    j_index = j + offset_dict[j]
                    if not selected[j]:
                        curr_edge_id = graph[i][j_index][1]
                        curr_edge_weight = graph[i][j_index][3]
                        if minimum > curr_edge_weight:
                            minimum = curr_edge_weight
                            x = i
                            y = j
                            y_index = j_index
                            edge_id = curr_edge_id
                            weight = curr_edge_weight
                            
        # print(selected[y])
        # print(y_index)
        tree_edges.append((edge_id, x, y, weight))
        total_weight += graph[x][y_index][3]
        selected[y] = True
        no_edge += 1

    
    # ** return the edge IDs themselves

    return total_weight, tree_edges