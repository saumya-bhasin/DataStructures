#Reverse digits of an integer.

#Example1: x = 123, return 321
#Example2: x = -123, return -321 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag,a=False,0
        if x<0:
            x=x*(-1)
            flag= True
        
        while x > 0:
            a=a*10+x%10
            x=x/10
        
        if a > 0x7FFFFFFF:
            return 0

        if flag == True:
            return (-1)*a
        else:
            return a
 
x=-123
print Solution().reverse(x)
