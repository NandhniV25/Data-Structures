class Node:
    def __init__(self, val, next):
        self.val = val 
        self.next = next

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self,v):
        if self.head==None:
            self.head=Node(v,None)
            self.tail=self.head
        else:
            self.tail.next=Node(v,None)
            self.tail=self.tail.next
    def dequeue(self):
        if self.head==None:
            print("Queue is empty")
        else:
            val=self.head.val
            self.head=self.head.next
            if self.head==None:
                self.tail==None
        return val
    def isempty(self):
        return self.head==None 
n=Queue()
n.enqueue(2)
n.enqueue(4)
n.enqueue(4)
a=n.dequeue()
print(a)
a=n.dequeue()
print(a)
b=n.isempty()
print(b)
a=n.dequeue()
print(a)
a=n.dequeue()
print(a)
b=n.isempty()
print(b)