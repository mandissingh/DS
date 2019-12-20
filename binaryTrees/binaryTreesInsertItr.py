class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def inOrder(self):
    self.inOrder(self.root)

  def inOrder(self, t):
    if(t):
      self.inOrder(t.left)
      print(t.data,end = " ")
      self.inOrder(t.right)
    else: return

  def insert(self, data):
    new_node = Node(data)
    if(self.root == None):
      self.root = new_node
      return
    t = self.root
    while(t):
      x = t
      if(data < t.data):
        t = t.left
      else:
        t = t.right

    if(data < x.data):
      x.left = new_node
    else:
      x.right = new_node
    return x
    


bt = BinaryTree()
bt.insert(1)
bt.insert(5)
bt.insert(3)
bt.insert(9)
bt.insert(6)
bt.inOrder(bt.root)