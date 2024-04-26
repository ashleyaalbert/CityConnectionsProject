def dijkstra(graph, length):

    # Initializing source, distances as a large number, visited list to false and the list 
    # and total weight to hold returning information
    src = 0
    distance = [1000000 for _ in range(length)]
    distance[src] = 0
    visited = [False for _ in range(length)]
    the_list = []
    total_weight = 0


    # Loop through the nodes and pick the next node based on distance to visit
    for _ in range(length):
        # No start node yet
        start = -1
        # Checking to see if the nodes have been visited or not
        for i in range(length):
            # Node[i] hasn't been visited or processed, or distance is less
            if not visited[i] and (start == -1 or (distance[i] < distance[start])):
                start = i
        
        # If we looped through and we can't reach a node we break
        if distance[start] == 1000000:
            break
        visited[start] = True

        # Labelling the different indexes of the list of adjacent edges
        for list_of_adjacent_edges in graph[start]: 
            id = list_of_adjacent_edges[0]
            begin = list_of_adjacent_edges[1]
            end = list_of_adjacent_edges[2]
            weight = list_of_adjacent_edges[3]

            # Comparing distances from the start node to distances we already have of it
            if distance[start] + 1 < distance[end]:
                distance[end] = distance[start] + 1
                total_weight += weight
                the_list.append((id, begin, end, weight))

    # Return the total weight and the ids, starting nodes, ending nodes, and weights
    return total_weight, the_list