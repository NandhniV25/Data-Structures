from queue import Queue
class BTNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left 
        self.right=right
def inorder(node):
    if node==None:
        return 
    inorder(node.left)
    print(node.val,end="->")
    inorder(node.right)
def preorder(node):
    if node==None:
        return 
    print(node.val,end="->")
    preorder(node.left)
    preorder(node.right)
def postorder(node):
    if node==None:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.val,end="->")
def levelorder(node):
    q=Queue()
    q.put(node)
    while not q.empty():
        n=q.get()
        print(n.val,end="->")
        if n.left!=None:
            q.put(n.left)
        if n.right!=None:
            q.put(n.right)
    print()
n1=BTNode(1)
n2=BTNode(2)
n3=BTNode(3)
n4=BTNode(4)
n5=BTNode(5)
n6=BTNode(6)
n7=BTNode(7)
n8=BTNode(8)
n9=BTNode(9)
n10=BTNode(10)
n1.left=n2
n1.right=n3   
n2.left=n6
n6.left=n4
n3.left=n5
n3.right=n7
n5.left=n8
n7.left=n9
n7.right=n10
print("in")
inorder(n1)
print("\npre")
preorder(n1)
print("\npost")
postorder(n1)
print("\nlevel")
levelorder(n1)