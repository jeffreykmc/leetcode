#1688. Count of Matches in Tournament

class Solution:
    def numberOfMatches(self, n: int) -> int:
        count=0
        m=n
        while True:
            left=m%2
            thiscount=m//2
            m=thiscount
            m+=left
            count+=thiscount
            print(m,left,count,thiscount)
            if m<2:
                break
        return count