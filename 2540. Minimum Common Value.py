#2540. Minimum Common Value
#https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2024-03-09

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a=sorted(set(nums1).intersection(nums2))
        if len(a)==0:
            return -1
        return a[0]

'''        
        x=min(nums1)
        y=min(nums2)
        if x>y:
            for a in sorted(nums1):
                if a in nums2:
                    return a
        else:
            for a in sorted(nums2):
                if a in nums1:
                    return a
        return -1
'''
'''
        a=Counter(nums1+nums2)

        for b in sorted(a, key=a.get, reverse=True):
            if a[b]==2:
                return b
        return -1
'''

