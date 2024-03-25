#238. Product of Array Except Self
#https://leetcode.com/problems/product-of-array-except-self/description/?envType=daily-question&envId=2024-03-15


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        b=[1]*n
        cur=1
        for i in range(n):
            b[i]=cur
            cur*=nums[i]
        cur=1
        for i in range(n-1,0-1,-1):
            b[i]*=cur
            cur*=nums[i]
        return b
    


#error TLE
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        b=[]*n
        for i in range(n):
            totalsum=1
            for k in range(n):
                if k!=i:
                    totalsum*=nums[k]
            b[i]=totalsum
        return b