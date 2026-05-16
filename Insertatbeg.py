class Node :
  def __init__(self ,data):
    self.data = data
    self.next = None

class LinkedList :
  def __init__(self):
    self.head = None
  
  def Append(self , data,):
    newNode = Node(data)
    if self.head == None:
      self.head = newNode
      return
    curr = self.head
    while curr.next != None:
      curr = curr.next
    curr.next = newNode
    
  def insertatbeg(self,data):
    newNode = Node(data)
    prevvalue = self.head
    self.head = newNode
    curr = self.head
    curr.next = prevvalue
    
  def display(self):
    curr = self.head
    while curr != None:
      print(curr.data,"->")
      curr = curr.next
    print("None")
    

a = LinkedList()
n = int(input("enter the number of nodes u wanna enter"))
for i in range(n):
  val = int(input("enter the value"))
  a.Append(val)

a.display()

choice = int(input("enter the 1 if u wanna insert a node at beg"))
if choice ==1:
  c = int(input("enter the value u wanna inset at beg"))
  a.insertatbeg(c)
  a.display()
else:
  print("exiting program")
  exit(0)
  
  