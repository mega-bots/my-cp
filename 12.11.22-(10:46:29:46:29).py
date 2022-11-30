class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = Node()
    def insert(self,data):
        if self.head.data == None:
            self.head.data = data
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = Node(data)
    def display(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end = " ")
            temp = temp.next
a = Linkedlist()
a.insert(3)
a.insert(5)
a.insert(2)
a.display()


class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = Node()
    def insert(self,ele):
        temp = self.root
        if temp.data == None:
            self.root.data = ele
        else:
            while(temp!=None):
                prev = temp
                if ele>temp.data:
                    temp = temp.right
                elif ele<temp.data:
                    temp = temp.left
            if ele>prev.data:
                prev.right = Node(ele)
            else:
                prev.left = Node(ele)
    def inorder(self):
      def Inorder(head):
        if head!=None:
            Inorder(head.left)
            print(head.data,end = " ")
            Inorder(head.right)
      Inorder(self.root)
print()
a = BinarySearchTree()
n = int(input("enter the number of numbers to be inserted: "))
for i in range(n):
    ele = int(input("Element{0}:".format(i+1)))
    a.insert(ele)
a.inorder()
            
    










        
            
            
        
        
