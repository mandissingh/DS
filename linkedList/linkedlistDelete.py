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

  def deleteNode(self, index):
    if(index < 1):
      print("Index Out of range")
      return
    t = self.head
    if index == 1:
      self.head = t.next
      t = None
      return
    while(index != 1 and t != None):
      index -= 1
      prev = t
      t = t.next
    if(t == None):
      print("Index Out of range")
      return
    prev.next = t.next
    t = None
    return
    
  def deleteDataNode(self, data):
    t = self.head
    while(t):
      if(self.head.data == data and t == self.head):
        self.head = self.head.next
        t = None
        return
      if(t.next != None and t.next.data == data):
        free = t.next
        t.next = t.next.next
        free = None
        return
      t = t.next
    print("Element not in list")
    return

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
llist.deleteDataNode(7)
printList(llist.head)