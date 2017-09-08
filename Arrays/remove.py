#27 Remove element

def Remove(arr,val):

    k=0
    for i in range(1,len(arr)):
        if arr[k]==val and arr[i]!=val:
            arr[k]=arr[i]
            arr[i]=val
            k+=1
    arr[k:]=""

    print arr

arr=[1,5,1,3,4,1,5,6,7,8,9,1]
Remove(arr,1)