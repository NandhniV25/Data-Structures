class Node:
    def __init__(self,val,next):
        self.val=val
        self.next=next
    def printfn(self):
        dummy=self
        while dummy!=None:
            print(dummy.val,end="->")
            dummy=dummy.next
        print()
    def insert_at_pos(self,val,pos):
        if pos==0:
            return Node(val,self)
        dummy=self
        ind=0
        prev=Node(0,None)
        while not(dummy==None or ind==pos):
            prev=dummy
            dummy=dummy.next
            ind+=1
        if ind==pos:
            prev.next=Node(val,dummy)
        else:
            print("out of index")
        return self
    def insert_at_order(self,val):
        dummy=self
        if dummy.val>=val:
            return Node(val,self)
        prev=Node(0,None)
        #while not (dummy==None or dummy.val>=val):
        while dummy!=None and dummy.val<=val:
                prev=dummy
                dummy=dummy.next
        prev.next=Node(val,dummy)
        return self
class PriorityQ:
    def __init__(self):
        self.head=None
    def enqueue(self,val):
        if self.head==None:
            self.head=Node(val,None)
        else:
            self.head=self.head.insert_at_order(val)
    def dequeue(self):
        dummy=self.head
        self.head=self.head.next
        return dummy.val
    def isempty(self):
        return self.head==None
n1=PriorityQ()
n1.enqueue(5)
n1.enqueue(3)
n1.enqueue(2)
n1.enqueue(1)
n1.enqueue(6)
n1.enqueue(10)
n1.enqueue(7)
a=n1.dequeue()
print(a)
a=n1.dequeue()
print(a)
a=n1.dequeue()
print(a)
a=n1.dequeue()
print(a)
a=n1.dequeue()
print(a)
a=n1.dequeue()
print(a)
a=n1.dequeue()
print(a)
a=n1.dequeue()
print(a)
