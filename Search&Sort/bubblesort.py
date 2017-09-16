#Implement bubble sort

class Sort:
    def bubblesort(self,arr):
        n=len(arr)

        while n>1:
            i=1
            while i<n:
                if arr[i]<arr[i-1]:
                    temp=arr[i-1]
                    arr[i-1]=arr[i]
                    arr[i]=temp
                i+=1
            n-=1
        print arr
    
    def bubble(self,arr):
        n=len(arr)

        while n>1:
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    temp=arr[i]
                    arr[i]=arr[i+1]
                    arr[i+1]=temp
            n-=1
        print "arr ",arr

    def bubblesortRec(self,arr,n):

        if n==1:
            return 

        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
        
        self.bubblesortRec(arr,n-1)

arr=[5,4,2,9]
#Sort().bubblesort(arr)
#Sort().bubblesortRec(arr,len(arr))
Sort().bubble(arr)
#print "arr ",arr