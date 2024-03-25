#442. Find All Duplicates in an Array
#https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25



class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
#https://leetcode.com/problems/find-all-duplicates-in-an-array/solutions/4921192/easy-solution-time-o-n-space-o-1-c-java-python3-kotlin/?envType=daily-question&envId=2024-03-25
        result = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0:
                #same index flipped before.
                result.append(num)
            nums[idx] *= -1
        return result