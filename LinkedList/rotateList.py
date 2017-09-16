#Rotate list
from SLL import LinkedList

class rotateList(object):
    def rotate(self,l,k):

        for i in range(0,k):
            p=l.start
            q=l.start

            while q.next is not None:
                q=q.next        

            q.next=p
            temp=p
            p=p.next
            l.start=p
            temp.next=None
        
        p=l.start
        while p is not None:
            print p.data,
            p=p.next


l=LinkedList()
#l.append(9)
l.append(7)
l.append(6)
l.append(9)
l.append(5)
l.append(1)
l.printlist()

rotateList().rotate(l,2)