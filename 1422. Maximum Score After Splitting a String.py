#1422. Maximum Score After Splitting a String
#https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=daily-question&envId=2023-12-22

class Solution:
    def maxScore(self, s: str) -> int:
        maxC=0
        ls=len(s)
        for i in range(1,ls):
            maxC=max(maxC,s[:i].count('0')+s[-(ls-i):].count('1'))
            #leftS=s[:i]
            #rightS=s[-(len(s)-i):]
            #print(i,leftS,rightS,leftS.count('0')+rightS.count('1'))
            #maxC=max(maxC,leftS.count('0')+rightS.count('1'))
        return maxC


