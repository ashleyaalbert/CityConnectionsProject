from parse import *
from prim import *
from krus import *
from dijk import *
# from visualize import *

def main():
    # Prompt user for a file name
    result = False
    while result is False:
        fileName = input("Enter the name of your graph file: ")
        result = promptForFile(fileName)
    
    # Create adjacency list to represent the graph
    graph = create_graph(fileName)

    # Run Dijkstra's algorithm and write output to dijkstra_output.txt"
    print("Running Dijkstra's algorithm...")
    total_weight, tree_edges = dijkstra(graph, len(graph))
    writeToFile(total_weight, tree_edges, "dijkstra.txt")

    # Run Kruskal's algorithm and write output to "kruskal_output.txt"
    print("Running Kruskal's algorithm...")
    total_weight, tree_edges = kruskal(graph, len(graph))
    writeToFile(total_weight, tree_edges, "kruskal.txt")

    # Visualize, but only a portion, not thousands:
    # G = GraphVisualization() 
    # with open("workingSmallTest.txt", 'r') as file:
    #     for line in file:
    #         id, start, end, weight = line.split()
    #         start = int(start)
    #         end = int(end)
    #         weight = float(weight)
    #         G.addEdge(start, end)
    # G.visualize() 
print("HELLO")

# Write algorithm output to a file
def writeToFile(total_weight, tree_edges, output_file):
    output = open(output_file, 'w')
    new_str = ""
    counter = 0
    for edge in tree_edges:
        new_str = str(edge[0]) + " " + str(edge[1]) + " " + str(edge[2]) + " " + str(edge[3])
        output.write(new_str)
        counter += 1
        if (counter < len(tree_edges)):
            output.write("\n")

    output.close() 
    print("The edges are in the file " + output_file)
    print("Total number of edges is " + str(counter))
    print("Total weight is " + str(total_weight) + "\n")


# Validate the file format
def promptForFile(fileName):
    if not os.path.exists(fileName):
        print("File does not exist. Please try again.")
        return False

    with open(fileName, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() != "":
                return True
    print("File is empty. Please try again.")
    return False
  
main()