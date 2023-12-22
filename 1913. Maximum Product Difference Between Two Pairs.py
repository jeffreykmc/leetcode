#1913. Maximum Product Difference Between Two Pairs
#https://leetcode.com/problems/maximum-product-difference-between-two-pairs/?envType=daily-question&envId=2023-12-18

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        snums=sorted(nums)
        l=len(nums)
        w=snums[0]
        x=snums[1]
        y=snums[-1]
        z=snums[l-2]
        print(w,x,y,z)
        return y*z-w*x