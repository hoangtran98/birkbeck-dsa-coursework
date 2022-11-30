class AdjNode:
  def __init__(self, data):
    self.vertex = data
    self.next = None

class Graph:

  def __init__(self, vertices):
    self.V = vertices
    self.graph = [None] * self.V

  # add an edge in an undirected graph
  def add_edge(self, src, dest):
    # add dest node to the source node
    node = AdjNode(dest)
    node.next = self.graph[src]
    self.graph[src] = node

    # add the source node to the dest node
    node = AdjNode(src)
    node.next = self.graph[dest]
    self.graph[dest] = node
  
  def print_graph(self):
    for i in range(self.V):
      print(i, end=" ")

      node = self.graph[i]

      while node:
        print(node.vertex, end=" ")        
        node = node.next

      print('\n')
# def BFS(graph: Graph, src, parents=[]):
  
  print(src, end=' ')
  parents.append(src)

  temp = graph[src]
  
  children = []

  while temp:
    if temp.vertex in parents:
      continue

    print(temp.vertex, end=' ')
    children.append(temp.vertex)
  
  for c in children:
    BFS(graph, c, parents)

if __name__ == "__main__":
  V = 5
  graph = Graph(V)
  graph.add_edge(0, 1)
  graph.add_edge(0, 4)
  graph.add_edge(1, 2)
  graph.add_edge(1, 3)
  graph.add_edge(1, 4)
  graph.add_edge(2, 3)
  graph.add_edge(3, 4)

  graph.print_graph()
