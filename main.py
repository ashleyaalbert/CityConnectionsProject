from parse import *


# TODO: PROMPT: You should read in an input file in this format, build a representation of the graph, compute your shortest connecting set
# of edges, and write it out as a file in the same format.

# TODO: run the program in terminal by typing: python main.py
def main():
    # TODO: maybe prompt user for file otherwise use default one
    fileName = "smallTest.txt"
    # fileName = "californiaNetwork.txt"
    graph = create_graph(fileName)


    # TODO: example of looping through graph / accessing things since dictionaries/tuples can be wck
        # remember that each vertex is a key with a value of the form [(ID, end vertex, weight), (id2, v2, w2), ...]
    for key in graph:
        val = graph[key]
        if val != []:
            # print(val[0][2]) # prints weight of an edge
            pass

    # call alg 1

    # call alg2


    # output: just write the edges to an outputfile in same format as input files

main()