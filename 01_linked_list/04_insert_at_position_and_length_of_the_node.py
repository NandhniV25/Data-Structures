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
    def insert_At(self,v,position):
        dummy=self
        ind=0
        if position==0:
            return Node(v,self)
        while ind<position-1:
            ind+=1
            dummy=dummy.next
            if dummy==None:
                print("Index reached")
                return self
        next=dummy.next
        dummy.next=Node(v,next)
        return self
    def insert_At_rec(self,v,pos):
        if pos==0:
            return Node(v,self)
        if pos==1:
            dummy=self
            next=dummy.next
            dummy.next=Node(v,next)
            return self
        else:
            if self.next==None:
                print("index out of range")
                return self
            self.next.insert_At_rec(v,pos-1)
            return self
n1=Node(1,Node(2,Node(3,Node(4,None))))
n1.printfn()
n1=n1.insert_At(9,2)
n1=n1.insert_At(6,1)
n1=n1.insert_At(114,8)
n1=n1.insert_At(114,0)
n1.printfn()
n1=n1.insert_At_rec(3,13)
n1.printfn()