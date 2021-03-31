class Node:
  def __init__(self, data):
    self.vertex = data
    self.next = None


class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.vertices = [None] * self.V

  def addEdge(self, src, dest):
    node = Node(dest)
    node.next = self.vertices[src]
    self.vertices[src] = node
    
    node = Node(src)
    node.next = self.vertices[dest]
    self.vertices[dest] = node

  def printGraph(self):
    for i in range(self.V):
      print("Neighbours of {}: Head".format(i), end = "")
      t = self.vertices[i]
      while(t):
        print("-->{}".format(t.vertex),end = "")
        t = t.next
      print()


g = Graph(6)
g.addEdge(1,2)
g.addEdge(1,5)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.printGraph()
      
    