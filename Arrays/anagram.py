#find if two strings are anagram

def anagram(s1,s2):

    s1=s1.replace(' ','')
    s2=s2.replace(' ','')

    d={}

    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i in s2:
        if i in d:
            d[i]-=1
        else:
            d[i]=1
    
    for i in d:
        if d[i]!=0:
            return False
    return True

      
print anagram("abc","cba")
print anagram("abc","cbac")