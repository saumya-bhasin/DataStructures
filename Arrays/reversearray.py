#reverse array

def reverse(arr):

    i,j=0,len(arr)-1
    
    while i<j:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j-=1
        i+=1

    print arr

arr=[10,20,30,40,50,60,70,80,90,100]
reverse(arr)