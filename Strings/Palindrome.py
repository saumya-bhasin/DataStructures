class Solution(object):
    def isPalin(self,s):

        for i in range(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False

        return True

print Solution().isPalin("abcd")
print Solution().isPalin("aabdbaa")
print Solution().isPalin("a s d h d s a")
