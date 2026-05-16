class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
      
    def display(self):
      current = self.head
      while current != None:
        print(current.data, end=" -> ")
        current = current.next
      print("None")
      
l1 = LinkedList()
n = int(input("enter the number of nodes"))
for i in range (n):
  val = int(input(f"enter the value of {i+1} node"))
  l1.append(val)
  
print("Linked list is :")
l1.display()