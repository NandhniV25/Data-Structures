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
    def update(self,v,pos):
        dummy=self
        ind=0
        while ind<pos and dummy!=None:
            ind+=1
            dummy=dummy.next
        if dummy!=None:
            dummy.val=v
        else:
            print("out ofindex")
      
n1=Node(1,Node(2,Node(3,Node(4,None))))
n1.printfn()
n1.update(4,2)
n1.printfn()
n1.update(5,38)
n1.printfn()
