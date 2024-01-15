#1657. Determine if Two Strings Are Close
#https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=daily-question&envId=2024-01-14

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1=len(word1)
        l2=len(word2)
        b={}
        c={}
        if l1!=l2:
            return False
        for i in range(l1):
            try:
                b[word1[i]]+=1
            except:
                b[word1[i]]=1
            try:
                c[word2[i]]+=1
            except:
                c[word2[i]]=1
        count=0
        j=[]
        k=[]
        try:
            for d in b:
                j.append(b[d])
                k.append(c[d])
        except:
            return False
        if sorted(j)!=sorted(k):
            return False  
        return True