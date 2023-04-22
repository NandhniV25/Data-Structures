class Node:
    def __init__(self,val,next):
        self.val=val 
        self.next=next
    def insert_Last(self,v):
        dummy=self
        while dummy.next!=None:
            dummy=dummy.next
        dummy.next=Node(v,None)
    def insert_Last_rec(self,v):
        if self.next!=None:
            self.next.insert_Last_rec(v)
        else:
            self.next=Node(v,None)
    def print_fn(self):
        dummy=self
        while dummy!=None:
            print(dummy.val,end="->")
            dummy=dummy.next
        print()
n1=Node(1,(Node(2,(Node(3,None)))))
n1.print_fn()
n1.insert_Last(4)
n1.print_fn()
n1.insert_Last_rec(5)
n1.print_fn()
