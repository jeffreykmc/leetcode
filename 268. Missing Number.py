#268. Missing Number
#https://leetcode.com/problems/missing-number/description/?envType=daily-question&envId=2024-02-20



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            print(i, nums[i])
            if i != nums[i]:
                return i
        return len(nums)
    

#understand the pattaren 1+2+3+4+5
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n* (n+1) // 2 ) - sum(nums)