#2706. Buy Two Chocolates
#https://leetcode.com/problems/buy-two-chocolates/

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sprices=sorted(prices,reverse=True)
        print(sprices)
        w=len(prices)
        maxM=money+1
        m=0
        for j in range(w-1):
            if sprices[j]<money:
                m=sprices[j]
                for k in range(j+1,w):
                    if (sprices[k]+m)<=money:
                        if sprices[k]+m<=maxM:
                            maxM=sprices[k]+m
        if maxM==money+1:
            return money
        else:
            return money-maxM                
