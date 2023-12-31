#1624. Largest Substring Between Two Equal Characters
#https://leetcode.com/problems/largest-substring-between-two-equal-characters/?envType=daily-question&envId=2023-12-31


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        charlist='abcdefghijklmnopqrstuvwxyz'
        #aW=([0] *26)
        cW=len(s)
        if cW==1:
            return -1
        if cW==2:
            return 0
        totalMax=0

        for c in charlist:
            if c in s and s.count(c)>=2:
                thiscount=0
                thisstop=0
                thismax=0
                for a in s:
                    thiscount+=1
                    if a==c:
                        if thisstop==0:
                            thisstop=thiscount
                        else:
                            thismax=thiscount-thisstop-1
                totalMax=max(totalMax,thismax)
        if totalMax==0:
            return -1    
        return totalMax

