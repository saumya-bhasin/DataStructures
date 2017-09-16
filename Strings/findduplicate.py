# If string has unique characters

def dup(s):
    d=[]
    for i in s:
        if i not in d:
            d.append(i)
        else:
            return "duplicate"
    
    return "no duplicates" 

print dup("abcdef")
print dup("abcc")
