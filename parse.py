import os.path

# Creates a graph by using an adjacency list given an input file of edges of the form: ID start end weight 
# Graph is of the form:
#       graph = {
#                 v1: [(id1, v3, w3), (id2, v2, w2)]
#                 v2: [(id3, v1, w2)]
#                 v3: []
#               }
def create_graph(fileName):
    graph = {}

    # TODO: should we validate input? apparently the input could have comments (lines starting with #)
            # so maybe we exclude lines that are blank / start with #
    with open(fileName, 'r') as file:
        for line in file:
            # Store parts of each edge
            id, start, end, weight = line.split()
            weight = float(weight)

            # Only add vertices that are not already in the graph
            if start not in graph:
                graph[start] = []
            
            if end not in graph:
                graph[end] = []

            # Create an adjacency list for each vertex of the form: (id, vertex, weight)
            if (id, end, weight) not in graph[start]:
                graph[start].append((id, end, weight))
            
            # TODO: not sure if we should do this since it'll mess up edge IDs / might not be what he wants use to do:
                #  Since the graph is undirected, we must add edges in both directions: v1 -> v2 implies v2 -> v1
            # if (start, weight) not in graph[end]:
            #     graph[end].append((id, start, weight))

    # TODO: this loop is here for debugging
    for node, edges in graph.items():
        print(f"Node {node}: {edges}")   

    return graph     

