
# -# ----------------------------------- Iterative Implementation of BFS --------------------------------------------- 

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
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print(bfs(graph, 1))


# $ python simple-bfs.py 
# 1->2->3->None

# T.C = O(V+E)
# where VV is the number of vertices and EE is the number of edges.
