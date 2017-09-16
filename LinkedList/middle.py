#Find middle of link list
from SLL import LinkedList

class middleList(object):
    def middle(self,l):
        p=l.start
        length=0

        while p is not None:
            length+=1
            p=p.next
        
        p=l.start
        i=0

        while i<(length/2):
            p=p.next
            i+=1
        
        return p.data
    
    #Another Solution
    def middlesoln(self,l):
        p=l.start
        q=l.start

        while q and q.next is not None:
            p=p.next
            q=q.next.next
        
        return p.data
            


l=LinkedList()
l.append(9)
l.append(8)
l.append(6)
l.append(5)
l.append(3)
l.append(2)
l.printlist()

print middleList().middle(l)
print middleList().middlesoln(l)
