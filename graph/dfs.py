from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        print(v, end=" ")
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self):
        visited = set()

        for vertex in list(self.graph):
            if vertex not in visited:
                self.DFSUtil(vertex, visited)


if __name__ == "__main__":
    g = Graph()

    g.addEdge(0, 1)
    g.addEdge(0, 9)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(9, 3)

    g.DFS()
