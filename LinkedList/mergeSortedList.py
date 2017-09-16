#Merge sorted list 
from SLL import LinkedList

class mergeSortedList(object):
    def merge(self,l,m):
        p=l.start
        q=m.start
        p1=p
        q1=q 

        while p and q is not None:
            if p.data < q.data:
                p1=p
                p=p.next
            else:
                q1=q.next
                p1.next=q
                q.next=p
                p1=p1.next
                q=q1
        
        if q:
            p1.next=q
        
        p=l.start
        while p is not None:
            print p.data,
            p=p.next
        
        


l=LinkedList()
#l.append(9)
#l.append(7)
#l.append(6)
l.append(9)
l.append(5)
l.append(1)
l.printlist()

m=LinkedList()
#m.append(9)
#m.append(8)
m.append(8)
m.append(3)
m.append(2)
m.printlist()

mergeSortedList().merge(l,m)



#k.printlist()