class Node:
    def __init__(self, val, next):
        self.val = val 
        self.next = next
class Stack:
    def __init__(self):
        self.head=None
    def push(self,v):
        self.head=Node(v,self.head)
    def pop(self):
        if self.head==None:
            print("stack is empty")
        else:
            val=self.head.val
            self.head=self.head.next
            return val
    def isempty(self):
        return self.head==None
n=Stack()
n.push(2)
n.push(4)
n.push(4)
a=n.pop()
print(a)
a=n.pop()
print(a)
b=n.isempty()
print(b)
a=n.pop()
print(a)
a=n.pop()
print(a)
b=n.isempty()
print(b)