#Implementation of queue

class queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def enque(self,item):
        self.items.insert(0,item)

    def deque(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

q=queue()
print q.isEmpty()
q.enque(1)
q.enque(2)
q.enque(3)
print q.size()
print q.deque()
