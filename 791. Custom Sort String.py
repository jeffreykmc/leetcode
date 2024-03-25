#791. Custom Sort String
#https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        As=Counter(s)
        a=[]
        for o in order:
            i=s.count(o)
            if i>0:
                a.append(o*i)
                s=s.replace(o,'')
            if len(s)==0:
                break
        return ''.join(a)+s
