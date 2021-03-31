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

  def minValue(self, root='first'):
    if(root == 'first'):
      return self.minValue(self.root)
    elif(root.left is None):
      return root
    else:
      return self.minValue(root.left)

  def maxValue(self, root='first'):
    if(root == 'first'):
      return self.maxValue(self.root)
    elif(root.right is None):
      return root
    else:
      return self.maxValue(root.right)

  def getNode(self, data, root='first'):
    if(root == 'first'):
      return self.getNode(data, self.root)
    if(data == root.data):
      return root
    elif(data < root.data):
      return self.getNode(data, root.left)
    elif(data > root.data):
      return self.getNode(data, root.right)

  def deleteNode(self, data, root='first'):
    if(root == 'first'):
      self.root = self.deleteNode(data, self.root)
      return
    if(root is None):
      return root
    if(data < root.data):
      root.left = self.deleteNode(data, root.left)
    elif(data > root.data):
      root.right = self.deleteNode(data, root.right)
    else:
      if(root.right is None):
        temp = root.left
        root = None
        return temp
      elif(root.left is None):
        temp = root.right
        root = None
        return temp
      temp = self.minValue(root.right)
      root.data = temp.data
      root.right = self.deleteNode(temp.data, root.right)
    return root

bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(4)
bt.insert(2)
bt.insert(7)
bt.insert(6)
bt.insert(8)
bt.insert(15)
bt.insert(12)
bt.insert(11)
bt.insert(13)
bt.insert(18)
bt.insert(20)
bt.inOrder()
print()
bt.deleteNode(10)
bt.inOrder()