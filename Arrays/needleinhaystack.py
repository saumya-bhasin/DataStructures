#28 implement strstr
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

def find(arr,sub):

    m=0
    for i in range(0,len(arr)):
        m=i

        for j in range(0,len(sub)):
            
            if arr[m]==sub[j]:
                if j == len(sub)-1:
                    return i
                m+=1
            else:
                break

print find("abcbd","bc")
