from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    """
    BFS function finds out all reachable vertices from a given source sorted by level by level.
    Only works for undirected graph
    """

    def BFS(self, s, visited):
        numVertices = max(self.graph) + 1
        visited = [False] * numVertices

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    """
    BFSDis prints out BFS traversal of any random graphs, connected or disconnected.
    """

    def BFSDis(self):
        numVertices = max(self.graph) + 1
        visited = [False] * numVertices

        for i in range(len(visited)):
            if visited[i] == False:
                self.BFS(visited[i], visited)


if __name__ == "__main__":
    g = Graph()

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal" " (starting from vertex 2)")
    g.BFS(2)
