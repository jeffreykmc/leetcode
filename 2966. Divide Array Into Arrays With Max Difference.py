#2966. Divide Array Into Arrays With Max Difference
#https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-02-01

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        x=len(nums)
        nums.sort()
        lis = [[0,0,0] for _ in range(int(x/3))]
        for i in range(int(x/3)):
            for j in range(3):
                lis[i][j]=nums.pop()
            if max(lis[i])-min(lis[i])>k:
                return []
        return lis
                



