class Node :
  def __init__(self,data):
    self.data = data
    self.next = None
    
class Linkedlist:
  def __init__(self):
    self.head = None
  
  def append(self,data):
    newnode = Node(data)
    
    if self.head == None:
      self.head = newnode
      return
    
    current = self.head
    while current.next != None:
      current = current.next
    current.next = newnode
  
  def display(self) :
    current = self.head
    while current!=None:
      print(f"{current.data},->")
      current = current.next      
    print("None")
    
  def counter(self):
    current = self.head
    count =0
    while current!=None:
      count = count +1
      current = current.next
    return count
      
  def insertatpos(self,pos,value,num):
    current = self.head
    for i in range(pos-1):
      current = current.next
    
    temp = current.next
    newnode = Node(value)
    current.next = newnode
    newnode.next = temp

        
a = Linkedlist()
num = int(input("enter the number of nodes"))
for i in range(num):
  val = int(input("enter the value of the node : "))
  a.append(val)

pos = int(input("Enter the position u wanna insert the element :"))
pos = pos - 1
value = int(input("Enter the value u wanna insert:"))
a.insertatpos(pos,value,num)
a.display()