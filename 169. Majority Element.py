#169. Majority Element
#https://leetcode.com/problems/majority-element/description/?envType=daily-question&envId=2024-02-12

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countn=Counter(nums)
        return sorted(countn,key=countn.get,reverse=True)[0]
