#check if string is palindrome
from stack import Stack

class palindrome:
    def check(self,s):
        s1=Stack()
        
        for i in s:
            s1.push(i)
        
        p=""
        while s1.isEmpty() is False:
            p+=s1.pop()
        
        if p==s:
            return "palindrome"
        else:
            return "not palindrome"
        #print "p ",p
        



s="abcbaa"
print palindrome().check(s)
