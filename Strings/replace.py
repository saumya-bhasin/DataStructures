
#Write a method to replace all spaces in a string with '%2e:


def replace(s):

    #solution 1
    s1=""
    for i in s:
        if i == " ":
            s1+='%20'
        else:
            s1+=i

    print "solution1 ",s1

    #solution 2
    l=list(s)
    for i in range(len(l)):
        if l[i] == " ":
            l[i] = "%20"

    s1=''.join(l)
    print s1

replace("saumya bhasin a d")