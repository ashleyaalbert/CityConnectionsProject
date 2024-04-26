from parse import *
from prim import *
from krus import *
from dijk import *
import sys

def mainForDemo():  
    # Validate correct number of arguments
    if (len(sys.argv) < 3):
        print("Please use the command in the form: python3 mainForDemo.py input.txt output.txt")
        exit()
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate correct file names
    if (input_file[-4:] != ".txt" or output_file[-4:] != ".txt"):
        print("Please enter files in the format: filename.txt")
        exit()
   
    # Validate file format
    if not checkFileFormat(input_file):
        exit()
    
    # Create adjacency list to represent the graph
    graph = create_graph(input_file)

    # Run Kruskal's algorithm and write output 
    total_weight, tree_edges = kruskal(graph, len(graph))
    writeToFile(total_weight, tree_edges, output_file)


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

    # print("The edges are in the file " + output_file)
    # print("Total number of edges is " + str(counter))
    # print("Total weight is " + str(total_weight))


# Validate the file format
def checkFileFormat(fileName):
    if not os.path.exists(fileName):
        print("File does not exist. Please try again.")
        exit()

    with open(fileName, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() != "":
                return True
        print("File is empty. Please try again.")
        exit()


mainForDemo()