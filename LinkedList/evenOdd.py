#check if link list is even or odd
from SLL import LinkedList

class evenOdd(object):
    def check(self,l):
        p=l.start

        while p and p.next:
            p=p.next.next
     
        if p:
            return "odd"
        else:
            return "even"


l=LinkedList()
#l.append(9)
l.append(7)
l.append(6)
l.append(9)
l.append(5)
#l.append(1)
l.printlist()

print evenOdd().check(l)


    