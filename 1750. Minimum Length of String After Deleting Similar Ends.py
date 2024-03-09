#1750. Minimum Length of String After Deleting Similar Ends
#https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/?envType=daily-question&envId=2024-03-05

class Solution:
    #https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/solutions/4824247/worst-solution-ever-but-explantion-is-good/?envType=daily-question&envId=2024-03-05
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            ch = s[l]
            while l <= r and s[l] == ch:
                l += 1
            while l <= r and s[r] == ch:
                r -= 1
        return  r - l + 1
    
