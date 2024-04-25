from parse import *
from prim import *
from krus import *
from dijk import *

def main():
    # TODO: prompt user for file otherwise use default one, validate input
    #fileName = "workingSmallTest.txt"
    # fileName = "smallTest.txt"
    #fileName = "californiaNetwork.txt"
    # fileName = "roads.txt"
    #fileName = "tricktest.txt"
    
    # Create adjacency list to represent the graph
    graph = create_graph(fileName)

    # Run Dijkstra's algorithm and write output to dijkstra_output.txt"
    # total_weight, tree_edges = dijk(graph, len(graph))
    # writeToFile(total_weight, tree_edges, "dijkstra_output.txt")

    # Run Kruskal's algorithm and write output to "kruskal_output.txt"
    total_weight, tree_edges = kruskal(graph, len(graph))
    writeToFile(total_weight, tree_edges, "kruskal_output.txt")

def writeToFile(total_weight, tree_edges, output_file):
    output_file = open(output_file, 'w')
    new_str = ""
    counter = 0
    avg = 0
    for edge in tree_edges:
        new_str = str(edge[0]) + " " + str(edge[1]) + " " + str(edge[2]) + " " + str(edge[3])
        output_file.write(new_str)
        counter += 1
        if (counter < len(tree_edges)):
            output_file.write("\n")

    print("Total weight is " + str(total_weight))
    output_file.close() 

    # TODO: delete dis lol it's to find the average weight per edge for shits and giggles
    # with open("californiaNetwork.txt", 'r') as file:
    #     total = 0
    #     for line in file:
    #         id, start, end, weight = line.split()
    #         start = int(start)
    #         end = int(end)
    #         # a = float(weight)
    #         print(weight)
    #         total += float(weight)

    # print((total / 21693) * len(tree_edges))

  
main()