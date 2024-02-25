#231. Power of Two
#https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-02-19


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(32):
            if n == 2**x:
                return True
        return False
        
