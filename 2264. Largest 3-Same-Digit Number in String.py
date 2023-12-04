#2264. Largest 3-Same-Digit Number in String
#https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for a in "9876543210":
            if num.find(a*3)>=0:
                return a*3
        return ""
