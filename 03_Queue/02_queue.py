class Node:
    def __init__(self, val, next):
        self.val = val 
        self.next = next
    def insert_at_last(self, v):
        dummy=self
        while dummy.next!=None:
            dummy=dummy.next
        dummy.next=Node(v,None)
    def delete_at_front(self):
        return self.next,self.val
class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,v):
        if self.head==None:
            self.head=Node(v,None)
        else:
            self.head.insert_at_last(v)
    def dequeue(self):
        if self.head==None:
            print("Queue is empty")
        else:
            a=self.head.delete_at_front()
            self.head=a[0]
            return a[1]
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
b=n.isempty()
print(b)