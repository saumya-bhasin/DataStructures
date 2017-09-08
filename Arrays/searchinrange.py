#Search for a range
#Given [5, 7, 7, 8, 8, 10] and target value 8,
#return [3, 4]. 

def search(arr,val):
    l=[]

    if arr is []:
        l=[-1,-1]
        print l

    for i in range(len(arr)):
        if arr[i] == val:
            l.append(i+1)
            break
    for j in range(len(arr)-1,-1,-1):
        if arr[j] == val:
            l.append(j+1)
            break
    print l

nums=[5,7,7,8,8,8,10]
val=8
search(nums,val)
