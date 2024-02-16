#647. Palindromic Substrings
#https://leetcode.com/problems/palindromic-substrings/description/?envType=daily-question&envId=2024-02-10


class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkispalin(this):
            a=len(this)
            for t in range(a//2):
                if this[t]!=this[a-t-1]:
                    return False
            return True
        len_s=len(s)
        count=0
        for i in range(len_s):
            for j in range(1,len_s-i+1):
                thisS=s[i:i+j]
                if checkispalin(thisS):
                    count+=1
        return count
    