# ------------------------------------------------- Weighted Directed Graph Implementation -------------------------------------------------
# In a weighted graph, every edge has a weight or cost associated with it.

class Edge :
    def __init__(self, src, dest, weight) :
        self.src = src
        self.dest = dest
        self.weight = weight

class Node : 
    def __init__(self, value, weight) :
        self.value = value
        self.weight = weight

class Graph :
    def __init__(self, edges, N) :
        self.adj = [None] * N

        for i in range (N) :
            self.adj[i] = []

        for e in edges :
            node = Node(e.dest, e.weight) 
            self.adj[e.src].append(node)

def printgraph(graph) :
    for src in range(len(graph.adj)) :
        for edge in graph.adj[src] :
            print(f'({src} -> {edge.value}, {edge.weight})', end = '') 
        print()


def main() :
    edges = [
        Edge(0, 1, 6), Edge(1, 2, 7), Edge(2, 0, 5),
        Edge(2, 1, 4), Edge(3, 2, 10), Edge(4, 5, 1), 
        Edge(5, 4, 3)
    ]
    N = 6
    graph = Graph(edges, N)
    printgraph(graph)


if __name__ == '__main__' :
    main()


# $ python weighted-directed-graph.py
# (0 -> 1, 6)
# (1 -> 2, 7)
# (2 -> 0, 5)(2 -> 1, 4)
# (3 -> 2, 10)
# (4 -> 5, 1)
# (5 -> 4, 3)

# T.C = O(n) or O(n^2) not sure you suggest !


