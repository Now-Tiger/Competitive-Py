
# ----------------------------------- Iterative Implementation of BFS ------------------------------------------

from collections import deque

class Graph :
    def __init__(self, edges, N) :
        self.adjList = [[] for _ in range(N)]

        for (u, v) in edges :
            self.adjList[u].append(v)
            self.adjList[v].append(u)


def bfs(graph, node, visited):
    q = deque()
    visited[node] = True
    q.append(node)
 
    while q:
        s = q.popleft()
        print(s, end='->')
 
        # do for every edge `v —> u`
        for u in graph.adjList[s]:
            if not visited[u]:
                # mark it as discovered and enqueue it
                visited[u] = True
                q.append(u)


# Driver function

if __name__ == '__main__' :
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        ]
    
    N = 15
    
    graph = Graph(edges, N)
    
    visited = [False] * N
    
    print(bfs(graph, 1, visited))


# $ python bfs.py
# 1->2->3->4->5->6->7->8->9->10->11->12->None



