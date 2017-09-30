
#Determine whether an integer is a palindrome. Do this without extra space.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #solution1
        y=str(x)
        z= y[::-1]
        comp=cmp(z,str(x))
        return comp != 1
            
        
        #solution2(using integer)
        a,z=0,x
     
        while(x>0):
            a=a*10+x%10
            x=x/10
        
        return z == a
            



x=1212
print Solution().isPalindrome(x)
