#rotate an array with a given order

def rotate(arr,order):
    while order > 0:
        for i in range(len(arr)-1):
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
        order-=1

    return arr

arr = [1,2,3,4,5,6,7]
order = 3

print rotate(arr,order)
