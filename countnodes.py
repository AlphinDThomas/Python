class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
  
class Linkedlist:
  def __init__(self):
    self.head = None 
  
  def append(self, data):
    newnode = Node(data)
    if self.head == None:
      self.head = newnode
      return
    
    curr = self.head
    while curr.next != None:
      curr = curr.next
    curr.next = newnode
    
  def display(self):
    curr = self.head
    while curr != None:
      print(curr.data,"->")
      curr = curr.next
    print("None")
    
  def count(self):
    count =0
    curr = self.head
    while curr != None:
      count = count + 1
      curr = curr.next
    print(count)
  
a = Linkedlist()
n = int(input("enter the number of nodes u wanna enter : "))
for i in range(n):
  val = int(input("enter the value of the node :"))
  a.append(val)
  
a.count()