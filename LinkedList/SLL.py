#Program to implement operations of singlly link list.

class Node(object):
    def __init__(self,d,n):
        self.data=d
        self.next=n
    
    def getData(self):
        return self.data

    def setData(self,data):
        self.data=data
    
    def getNext(self):
        return self.next
    
    def setNext(self,next):
        self.next=next
    

class LinkedList(object):
    
    def __init__(self):
        self.start=None
        self.length=0

    def append(self,d):
        new_node=Node(d,self.start)
        self.start=new_node
        self.length+=1
        #print self.length
    
    def printlist(self):
        p=self.start
        #print self.length
        while p:
            print str(p.getData()),
            p=p.getNext()
        print ""

    def remove(self,position):
        k=1
        p=self.start
        if position == 1:
            self.start=p.getNext()
        else:
            while p and (k<position):
                q=p
                p=p.getNext()
                k+=1
            
            if p is None:
                return False
            else:
                q.setNext(p.getNext())
        
        return p.getData()


'''
l=LinkedList()
l.append(3)
l.append(5)
l.append(6)
l.append(7)
l.printlist()
print "removed ",l.remove(4)
l.printlist()
#print "removed ",l.remove(4)
#l.printlist()
'''