class Node:
    def __init__(self, val, next):
        self.val = val 
        self.next = next
    def insert_at_front(self, v):
        return Node(v,self)
    def delete_at_last(self):
        dummy = self 
        if self.next==None:
            return None,self.val
        while dummy.next.next!=None:
            dummy=dummy.next
        val=dummy.next.val
        dummy.next=None
        return self,val
class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,v):
        if self.head==None:
            self.head=Node(v,None)
        else:
            self.head=self.head.insert_at_front(v)
    def dequeue(self):
        if self.head==None:
            print("Queue is empty")
        a=self.head.delete_at_last()
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


================================================================================================

class Node:
    def __init__(self, val, next):
        self.val=val
        self.next=next
    def insert_last(self,val):
        dummy=self
        while dummy!=None and dummy.next!=None:
            dummy=dummy.next
        dummy.next=Node(val,None)
    def delete_front(self):
        return self.val,self.next
class Q:
    def __init__(self):
        self.head=None
    def enq(self,val):
        if self.head==None:
            self.head=Node(val,None)
        else:
            self.head.insert_last(val)
    def deq(self):
        if self.head==None:
            print("Queue is empty")
        a=self.head.delete_front()
        self.head=a[1]
        return a[0]
n=Q()
n.enq(2)
n.enq(4)
n.enq(4)
a=n.deq()
print(a)
a=n.deq()
print(a)
a=n.deq()
print(a)
a=n.deq()
print(a)