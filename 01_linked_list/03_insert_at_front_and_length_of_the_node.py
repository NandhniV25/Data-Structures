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
    def insert_front(self,v):
        return Node(v,self)
    def length_fn(self):
        dummy=self
        count=1
        while dummy.next!=None:
            count+=1
            dummy=dummy.next
        return count
    def length_rec(self):
        if self.next!=None:
            return 1+self.next.length_rec()
        else:
            return 1
n1=Node(1,Node(2,Node(3,Node(4,None))))
n1.printfn()
n1=n1.insert_front(9)
n1.printfn()
a=n1.length_fn()
print(a)
b=n1.length_rec()
print(b)



