#300. Longest Increasing Subsequence
#https://leetcode.com/problems/longest-increasing-subsequence/?envType=daily-question&envId=2024-01-05

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [0] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                 #   print("+",i,j,dp,nums[i],nums[j])
                #else:
                 #   print("-",i,j,dp,nums[i],nums[j])

        return max(dp)+1

