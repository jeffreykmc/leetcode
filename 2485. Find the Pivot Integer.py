#2485. Find the Pivot Integer
#https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13

class Solution:
    def pivotInteger(self, n: int) -> int:
        l=0
        r=n
        if n==1:
            return n
        suml=sumr=0
        while l<r:
            #print('=',l,r,suml,sumr)
            if sumr>suml:
                suml+=l
                l+=1
            #    print('l',l,r,suml,sumr)
            else:
                sumr+=r
                r-=1
            #    print('r',l,r,suml,sumr)
            if l==r:
                if suml==sumr:
                    return l
        return -1


