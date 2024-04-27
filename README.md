# Cities Connections

## Description
The Cities Connections Project analyzes and produces different algorithms for graphs in order to find the cheapest way, that costs the least amount of 
weight, to connect to every node. The algorithms print the total edge weight, in order to compare and find the cheapest path, and the number of edges used, 
to make sure that every vertex is being visited at least once. 
  The project consists of the two algorithms of Dijkstra’s and Kruskel’s. Dijkstra's algorithm finds the shortest weighted path in a graph from a source 
node and Kruskel’s uses a minimum spanning tree in order to find the shortest path. The system allows for a user to find the shortest weighted path using 
both Dijkstra and Kruskel’s algorithm. When running the system, the user will be prompted to enter the name of their text files, and they will be run 
through both algorithms if they are valid. It will then return the total number of edges used and the total weight of all of the edges. It will also produce 
a visualization of a minimum spanning tree on a given graph to show what exactly it would look like.

## Installation
In order to run this code, ensure that you have a recent version of Python3 downloaded onto your machine. 

## Downloading the repository
  To download this repo, simply clone the project:  
    cd repo_location  
    git clone https://github.com/cwc023/City_Connections_Project  


## Run the code  
Once the repo is downloaded, ensure that you are in the directory with the project files. From there, ensure that you have a recent version of Python3 downloaded. There are 2 different versions of the program you can run:  
1) Both algorithms + visualization  
  a) In order to run the visualization, you must first install the following Python modules:  
    i) **pip install networkx**    
    ii) **pip install scipy**    
    iii) **pip install matplotlib**    
  b) Type **python3 main.py** into the terminal    
  c) You will then be prompted to enter the name of the input file to run the algorithms on  
  d) The total edge weight and total edges used will be printed to the screen, with all of the edges used sent to the desired output file  
  e) By default, a visualization of a minimum spanning tree for the graph that represents the City of Oldenburg Road Network (~7,000 edges) is printed to the screen. The user can choose to print the minimum spanning tree from the output of Kruskal's algorithm instead (note: it may take over a minute for larger datasets).

3) Algorithm Competition: Kruskal’s algorithm  
  a) Type **python3 mainForDemo.py input.txt output.txt** into the terminal where **input.txt** is the name of the input file you’d like to run and **output.txt** is where you want the output to go.  
  b) The list of all used edges is sent to the desired output file  

## Authors and acknowledgment
Authors of this project include Ashley Albert, Connor Coles, Eric Reinhart, Harmony Yeung.

