#There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away.


class Test():
    def one(self, l1, l2):
        len1=len(l1)
        len2=len(l2)
        i,j,count=0,0,0

        if abs(len1-len2) >1:
            return False

        while i <len1 and j<len2:
            #print "i,j ",i,j
            if l1[i] == l2[j]:
                i+=1
                j+=1
            else:
                count+=1
                if len1>len2:
                    i+=1
                elif len1<len2:
                    j+=1
                else:
                    i+=1
                    j+=1
        
        #print "count ",count

        if count == 1 or count == 0:
            return True
        else:
            return False

l1="pales"
l2="pale"
print Test().one(l1,l2)