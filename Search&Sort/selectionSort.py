#implement selection sort
from sys import maxint

class selection:
    def sort(self,arr):
        i,k=0,0
        n=len(arr)

        while k<n:
            min=maxint
            for i in range(k,n):
                if min>arr[i]:
                    min=arr[i]
                    p=i
            if p!=k:
                t=arr[p]
                arr[p]=arr[k]
                arr[k]=t
            k+=1
        print "arr ",arr

arr=[64,25,12,22,11]
selection().sort(arr)
