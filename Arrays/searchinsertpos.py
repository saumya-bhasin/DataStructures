# Search insert position
#[1,3,5,6], 5 2
#[1,3,5,6], 2  1

def Search(nums,target):

    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i]>target:
            return i
        elif i+1==len(nums):
            return i+1

nums=[1,3,5,6]
target=7

print Search(nums,target)