#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#from stack import Stack

class validParentheses:
    def valid(self,s):
        s1=Stack()
        count=0

        for i in s:
            if i == '(' or i == '[' or i== '{':
                s1.push(i)
                count+=1
            elif i == ')':
                if s1.isEmpty() is True:
                    count+=1
                elif s1.pop() == '(':
                    count-=1
            elif i == ']':
                if s1.isEmpty() is True:
                    count+=1
                elif s1.pop() == '[':
                    count-=1
            elif i == '}':
                if s1.isEmpty() is True:
                    count+=1
                elif s1.pop() == '{':
                    count-=1



        if count == 0:
            return True
        else:
            return False

class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self,d):
        self.items.append(d)

    def pop(self):
        return self.items.pop()




s="([]})"
print validParentheses().valid(s)
