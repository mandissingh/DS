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


  def inserAtHead(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      return
    new_node.next = self.head
    self.head = new_node
    return

  def insertAfter(self, index, data):
    new_node = Node(data)
    t = self.head
    while(index > 1):
      t = t.next
      index -= 1
    new_node.next = t.next
    t.next = new_node
    return
    
############## Functions ###############

def printList(head):
  t = head
  while(t != None):
    print(t.data,end = " ")
    t = t.next
  print("\r")

############### Main code ###############

llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
printList(llist.head)
llist.inserAtHead(0)
llist.inserAtHead(-1)
llist.inserAtHead(-2)
printList(llist.head)
llist.insertAfter(5,22)
printList(llist.head)