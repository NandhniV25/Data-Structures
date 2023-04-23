class Node:
    def __init__(self,val,next):
        self.val=val
        self.next=next
    def insert_at_front(self,v):
        return Node(v,self)
    def delete_at_front(self):
        return self.next
class Stacka:
    def __init__(self):
        self.head=None
    def push(self,v):
        if self.head==None:
            self.head=Node(v,None)
        else:
            self.head=self.head.insert_at_front(v)
    def pop(self):
        if self.head==None:
            print("Stack is empty")
        val = self.head.val
        self.head=self.head.delete_at_front()
        return val
    def isempty(self):
        return self.head==None
        
st=Stacka()
b=st.isempty()
print(b)
st.push(2)
b=st.isempty()
print(b)
st.push(3)
b=st.isempty()
print(b)
st.push(10)
b=st.isempty()
print(b)
a=st.pop()
print(a)
a=st.pop()
print(a)
a=st.pop()
print(a)
b=st.isempty()
print(b)
a=st.pop()
print(a)