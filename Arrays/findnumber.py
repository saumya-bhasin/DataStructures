#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#For example,
#Given nums = [0, 1, 3] return 2. 

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=nums[len(nums)-1]

        for i in range(0,n+1):
            if i not in nums:
                return i
        
        return (nums[n]+1)       


nums=[0,1,3]
print Solution().missingNumber(nums)

