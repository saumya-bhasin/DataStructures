# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        count,l=0,0

        for i in nums:
            if i == 0:
                count+=1
            else:
                nums[l]=i
                l+=1
        
        for j in range(len(nums)-1,-1,-1):
            if count == 0:
                break
            else:
                nums[j]=0
                count-=1
        print nums

nums = [8,3,0,1,2,0]
Solution().moveZeroes(nums)