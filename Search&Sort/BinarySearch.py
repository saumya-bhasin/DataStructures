#implement binary search

class BinarySearch:
    def binary(self,arr,target):
        low,high=0,len(arr)-1

        while low<=high:
            mid=(low+high)/2

            if target == arr[mid]:
                return mid
            elif target>arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 10

print BinarySearch().binary(arr,x)