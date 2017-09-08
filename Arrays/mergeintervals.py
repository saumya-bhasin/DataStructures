#merge intervals in a given list

def merge(arr):
    i=0

    arr.sort()  #sort the array

    while i <= len(arr)-2:
        if arr[i][1]>arr[i+1][0] and arr[i][0]<arr[i+1][1]:
            arr[i][1]=max(arr[i+1][1],arr[i][1])   #take the maximum value
            arr.pop(i+1)
        else:
            i+=1

    print arr

arr=[[1,3],[2,4],[5,7],[6,9]]
merge(arr)
            
