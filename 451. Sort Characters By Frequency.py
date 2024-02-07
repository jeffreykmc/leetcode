#451. Sort Characters By Frequency
#https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=daily-question&envId=2024-02-07

class Solution:
    def frequencySort(self, s: str) -> str:
        cntS=Counter(s)
        #print(cntS)
        out=""
        for a in sorted(cntS,key=cntS.get,reverse=True):
            out+=a*cntS[a]
            #print(out)
        return out
    

#''.join(out) is faster than out+=string
class Solution:
    def frequencySort(self, s: str) -> str:
        cntS=Counter(s)
        #print(cntS)
        out=[]
        for a in sorted(cntS,key=cntS.get,reverse=True):
            out.append(a*cntS[a])
            #print(out)
        return ''.join(out)
