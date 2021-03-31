class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def inOrder(self, t='first'):
    if(t == 'first'):
      t = self.root
    if(t):
      self.inOrder(t.left)
      print(t.data,end = " ")
      self.inOrder(t.right)
    return

  def insert(self, data, root='first'):
    if(root == 'first'):
      self.root = self.insert(data, self.root)
      return
    if(root == None):
      new_node = Node(data)
      root = new_node
      return root
    elif(data < root.data):
      root.left = self.insert(data, root.left)
    elif(data > root.data):
      root.right = self.insert(data, root.right)
    return root



bt = BinaryTree()
bt.insert(7)
bt.insert(5)
bt.insert(3)
bt.insert(9)
bt.insert(6)
bt.inOrder(bt.root)