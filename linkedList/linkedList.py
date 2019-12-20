############### Node class ###############
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

############## LinkedList class ###############
class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      return
    t = self.head
    while(t.next != None):
      t = t.next
    t.next = new_node
    return

  def getCountItr(self):
    t = self.head
    count = 0
    while(t):
      count += 1
      t = t.next
    return count

  def getCountRec(self, node):
    if(node):
      return 1 + self.getCountRec(node.next)
    else:
      return 0

  def getCount(self):
    return self.getCountRec(self.head)
      


############## Functions ###############

def printList(head):
  t = head
  while(t):
    print(t.data,end = " ")
    t = t.next
  print("\r")

############### Main code ###############

llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(6)
llist.insert(7)
printList(llist.head)
print(llist.getCountItr())
print(llist.getCount())