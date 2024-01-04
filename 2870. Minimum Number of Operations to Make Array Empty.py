#2870. Minimum Number of Operations to Make Array Empty
#https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnums=Counter(nums)
        totalCount=0
        for c,k in cnums.items():
            b=k // 3   
            a=k % 3   
            if a>0:
                if b>=1:
                    b+=1
                elif a==2:
                    b+=1
                else:
                    return -1
            totalCount+=b

        return totalCount


