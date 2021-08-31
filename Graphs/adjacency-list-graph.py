
# Adjacency list implement in undirected graph

class Graph(object) :

    def __init__(self, Nodes) :
        self.nodes = Nodes
        self.adj_list = {}
        ''' Initially we initialize our adjacency list 
            as empty using dictionary here '''

        for node in self.nodes :
            self.adj_list[node] = []
            ''' We need to add all the vertices to our adjacency list, 
                at first these vertices are empty '''

    def add_edge(self, u, v) :
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_adj_list(self) :
        for node in self.nodes :
            print(node, ' -> ', self.adj_list[node])



nodes = ["A", "B", "C", "D", "E"]
all_edges = [('A', 'B'), ('A', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'E'), ('B', 'E')]

graph = Graph(nodes)

for u, v in all_edges :
    graph.add_edge(u, v)

graph.print_adj_list()


# $ python adjacency-list-graph.py 

# A  ->  ['B', 'C', 'D']
# B  ->  ['A', 'E']     
# C  ->  ['A', 'D']     
# D  ->  ['C', 'A', 'E']
# E  ->  ['D', 'B']

# T.c = O(n) 