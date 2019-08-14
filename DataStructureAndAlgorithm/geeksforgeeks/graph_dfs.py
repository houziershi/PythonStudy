# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        # Call the recursive helper function to print
        # DFS traversal
        self.child(visited, s)

    def child(self, visited, s):
        # Mark the current node as visited and print it
        visited[s] = True
        print(s, end=" ")
        # Recur for all the vertices adjacent to this vertex
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

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)
