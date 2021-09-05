
# ----------------------------------- Iterative Implementation of BFS --------------------------------------------- 

from collections import deque

def bfs(graph, root) :
    visited, queue = set(), deque([root])
    visited.add(root)

    while queue :
        s = queue.popleft()
        print(s, end = '->')

        for neighbour in graph[s] :
            if neighbour not in visited :
                visited.add(neighbour)
                queue.append(neighbour)


# Driver code :
if __name__ == '__main__' :
    g = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print(bfs(g, 1))

    print('--------------------\nAnother Example :\n-------------------- ')
   
    graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}
    print(bfs(graph, 'A'))


# $ python simple-bfs.py 
# 1 -> 2 -> 3 -> None
# --------------------
# Another Example :
# -------------------- 
# A -> B -> E -> C -> D -> F -> G -> None


# T.C = O(V+E)
# where V is the number of vertices and EE is the number of edges.
