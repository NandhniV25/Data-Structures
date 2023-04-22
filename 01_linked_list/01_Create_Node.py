class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def printnode(self):
        dummy=self
        while dummy!=None:
            print(dummy.val,end="->")
            dummy=dummy.next
        print()
    def rec_print(self):
        print(self.val,end="->")
        if self.next!=None:
            self.next.rec_print()
        else:
            print()
def Print_Fun(node):
    dummy=node
    while dummy!=None:
        print(dummy.val,end="->")
        dummy=dummy.next
    print()
def Print_Rec(node):
    print(node.val,end="->")
    if node.next!=None:
        Print_Rec(node.next)
    else:
        print()
node1=Node(1,None)
node2=Node(2,None)
node1.next=node2
node2.next=Node(3,None)
node1.printnode()
node1.rec_print()
Print_Fun(node1)
Print_Rec(node1)