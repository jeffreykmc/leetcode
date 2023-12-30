#1897. Redistribute Characters to Make All Strings Equal
#https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/?envType=daily-question&envId=2023-12-30

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words)==1:
            return True
        aW=([0] *26)
        cW=len(words)
        for w in words:
            for a in w:
                aW[ord(a)-ord('a')]+=1
        x=max(aW)
        for i in range(26):
            if aW[i]>0:
                if aW[i]%cW!=0:
                    return False
                if aW[i]<cW:
                    return False
        return True
