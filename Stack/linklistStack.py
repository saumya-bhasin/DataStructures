#Link list implementation of stack

class StackNode:
    def __init__(self,d):
        self.data=d
        self.next=None

class Stack:
    def __init__(self):
        self.start=None
    
    def isEmpty(self):
        if self.start:
            return False
        else:
            return True
    
    def push(self,data):
        n=StackNode(data)
        n.next=self.start
        self.start=n
    
    def pop(self):
        if self.isEmpty():
            return "Empty Stack"
        temp=self.start
        self.start=self.start.next
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        return self.start.data


print Stack().isEmpty()
s=Stack()
s.push(1)
s.push(5)
s.push(7)
print "popped ",s.pop()
print s.peek()
print "empty ",s.isEmpty()