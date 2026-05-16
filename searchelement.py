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
      
  def searchelement(self,n,element):
    current= self.head
    position =0
    for i in range(n):
      if current.data == element:
        position =i
        return position
      current = current.next
        
a = Linkedlist()
num = int(input("enter the number of nodes"))
for i in range(num):
  val = int(input("enter the value of the node : "))
  a.append(val)

n = a.counter()
element = int(input("enter the element u wanna search :"))
position = a.searchelement(n,element)
print(f"Element found at position {position+1}")