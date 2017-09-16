#Implement a method to perform basic string compression using the counts
#of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.


def compress(s):
    count=1
    s1=""

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count+=1
        else:
            s1+=s[i]
            s1+=str(count)
            count=1

    s1+=s[i+1]
    s1+=str(count)

    return s1


print compress("aaabccd")