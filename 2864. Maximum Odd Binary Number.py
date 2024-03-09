#2864. Maximum Odd Binary Number
#https://leetcode.com/problems/maximum-odd-binary-number/description/?envType=daily-question&envId=2024-03-01

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a=Counter(s)
        return '1'*(a['1']-1)+'0'*a['0']+'1'

        

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if len(s)==1:
            return s
        b=''.join(sorted(s))
        if b[-2]=='1':
            return (b[-1]+b[:len(b)-1])[::-1]
        else:
            return b


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a=s.count('1')
        return '1'*(a-1)+'0'*(len(s)-a)+'1'

        