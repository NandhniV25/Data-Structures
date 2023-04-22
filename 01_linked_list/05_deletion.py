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
    def deletion(self,pos):
        if pos==0:
            return self.next
        dummy=self
        ind=0
        while ind<pos-1 and dummy!=None:
            ind+=1
            dummy=dummy.next
        if dummy!=None and dummy.next!=None:
            dummy.next=dummy.next.next
        else:
            print("out of index")
            return self
        return self
n1=Node(1,Node(2,Node(3,Node(4,None))))
n1.printfn()
n1=n1.deletion(3)
n1=n1.deletion(4)
n1.printfn()
n1=n1.deletion(0)
n1.printfn()

