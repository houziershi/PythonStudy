# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, s):
        visited = [False] * (len(self.graph))
        self.child(visited, s)

    def child(self, visited, s):
        visited[s] = True
        print(s, end=" ")
        for i in self.graph[s]:
            if visited[i] is False:
                self.child(visited, i)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.DFS(2)
