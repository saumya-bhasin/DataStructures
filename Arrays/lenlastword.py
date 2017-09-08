#Length of last word


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
                
        if len(s) == 0:
            return 0

        count=0
        flag=False
        for i in s[::-1]:            
            if i == " ":
                break
            else:
                count+=1

        return count

s=" a bhjk"
print Solution().lengthOfLastWord(s)



