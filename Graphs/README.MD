# Graphs :
![image](https://media.geeksforgeeks.org/wp-content/cdn-uploads/undirectedgraph.png) <br>
- A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph can be defined as :
- #### A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.
- In the above Graph, the set of vertices V = {0,1,2,3,4} and the set of edges E = {0 1, 1 2, 2 3, 3 4, 0 4, 1 4, 1 3}.

- Graphs are used to solve many real-life problems. Graphs are used to represent networks. The networks may include paths in a city or telephone network or circuit network. Graphs are also used in __social networks like linkedIn, Facebook.__ 
- __For example, in Facebook, each person is represented with a vertex(or node). Each node is a structure and contains information like person id, name, gender, locale etc.__

# Types of graphs :
__1. Undirected Graph :__
- In an undirected graph, nodes are connected by edges that are all bidirectional. For example if an edge connects node 1 and 2, we can traverse from node 1 to node 2, and from node 2 to 1.
- Ex. Above image is an example of an __Undirected Graph__.

__i. Connected graph :__ 
- A graph is connected when there is a path between every pair of vertices. In a connected graph there is no unreachable node.

__ii. Complete graph :__
- A graph in which each pair of graph vertices is connected by an edge. In other words,every node ‘u’ is adjacent to every other node ‘v’ in graph ‘G’. A complete graph would have n(n-1)/2 edges.

__iii. Biconnected graph :__
- A connected graph which cannot be broken down into any further pieces by deletion of any vertex. It is a graph with no articulation point.<br><br>

__2. Directed Graph :__ 
- In a directed graph, nodes are connected by directed edges – they only go in one direction. 
- For example, if an edge connects node 1 and 2, but the arrow head points towards 2, we can only traverse from node 1 to node 2 – __not in the opposite direction.__ <br>

![image](https://www.researchgate.net/profile/Panagiotis-Papapetrou/publication/262329292/figure/fig1/AS:392513438404615@1470593904634/Example-of-a-social-network-represented-by-a-directed-graph.png)

__i. Directed Acyclic graph :__
- It is a directed graph with no cycle. For a vertex ‘v’ in DAG there is no directed edge starting and ending with vertex ‘v’.

__ii. Tree :__ 
- A tree is just a restricted form of graph. That is, it is a DAG with a restriction that a child can have only one parent.<br><br>
 
# Types of Graph Representations :
__1. Adjacency List :__
- To create an Adjacency list, an array of lists is used. The size of the array is equal to the number of nodes.
- A single index, array[i] represents the list of nodes adjacent to the ith node.<br><br>

![image](https://cdn.programiz.com/sites/tutorial2program/files/adjacency-list.png)

__2. Adjacency Matrix :__
- An Adjacency Matrix is a 2D array of size V x V where V is the number of nodes in a graph. 
- A slot matrix[i][j] = 1 indicates that there is an edge from node i to node j.
- On right hand side of the graph is the Adjacency Matrix.<br><br> 

![image](https://workat.tech/images/ps/adjacency-list-to-adjacency-matrix.svg)


# What is searching in graph data structure?
- A graph search is an algorithm scheme that visits vertices or vertices and edges in a graph, in an order based on the connectivity of the graph. 
- The most general searches visit both edges and vertices.<br>

 __Two standard graph search techniques have been widely used :__<br><br>
## [Breadth-First Search (DFS)](https://en.wikipedia.org/wiki/Breadth-first_search) :
- Breadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored.
- __For example__, in a chess endgame a chess engine may build the game tree from the current position by applying all possible moves, and use breadth-first search to find a win position for white. Implicit trees (such as game trees or other problem-solving trees) may be of infinite size; breadth-first search is guaranteed to find a solution node[1] if one exists.<br><br>

__[BFS follows the following rules](https://www2.seas.gwu.edu/~ayoussef/cs6212/graphsearch.html) :__<br>
    
  1. Select an unvisited node s, visit it, have it be the root in a BFS tree being formed. Its level is called the current level.
  2. From each node x in the current level, in the order in which the level nodes were visited, visit all the unvisited neighbors of x. The newly visited nodes from this level form a new level that becomes the next current level.
  3. Repeat the previous step until no more nodes can be vsisted.
  4. If there are still unvisited nodes, repeat from Step 1.

## [Depth-First Search (BFS)](https://en.wikipedia.org/wiki/Depth-first_search) :
- Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.
- A version of depth-first search was investigated in the 19th century by French mathematician Charles Pierre Trémaux as a strategy for solving mazes.

__[DFS follows the following rules](https://www2.seas.gwu.edu/~ayoussef/cs6212/graphsearch.html):__<br>
  1. Select an unvisited node s, visit it, and treat as the current node.<br>
  2. Find an unvisited neighbor of the current node, visit it, and make it the new current node;<br>
  3. If the current node has no unvisited neighbors, backtrack to the its parent, and make that the new current node; Repeat the above two steps until no more nodes can be visited.<br>
  4. If there are still unvisited nodes, repeat from step 1.<br>
