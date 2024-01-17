#1207. Unique Number of Occurrences
#https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=daily-question&envId=2024-01-17


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        b={}
        c=[]
        for a in arr:
            try:
                b[a]+=1
            except:
                b[a]=1
        for a in b:
            #print('+',a,b[a],b,c)
            if b[a] in c:
            #    print(a,b[a],b,c)
                return False
            c.append(b[a])
        return True
