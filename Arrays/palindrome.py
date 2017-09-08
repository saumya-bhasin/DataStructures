
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
        if comp == 1:
            return False
        else:
            return True
        
        #solution2(using integer)
        a,z=0,x
     
        while(x>0):
            a=a*10+x%10
            x=x/10
        
        if z == a:
            return True
        else:
            return False



x=1212
print Solution().isPalindrome(x)