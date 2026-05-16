class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def append(self,data):
    newnode = Node(data)
    if self.head == None:
      self.head = newnode
      return
    current = self.head
    while current.next!=None:
      current = current.next
    current.next = newnode
  
  def delfirst(self):
    curr = self.head
    temp = curr.next
    self.head = temp
    
  def dellast(self):
    current = self.head
    while current.next != None:
      temp = current
      current = current.next
    temp.next = None
    
  def display(self):
    current = self.head
    while current!=None:
      print(f"{current.data} ->")
      current = current.next
    print("None")
    
a = LinkedList()
n = int(input("enter the number of nodes u wanna enter"))
for i in range(n):
  val = int(input("enter the value of this node"))
  a.append(val)
a.display()
a.dellast()
a.display()
  