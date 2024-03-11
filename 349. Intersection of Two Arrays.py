#349. Intersection of Two Arrays
#https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=daily-question&envId=2024-03-10

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(nums2)
    


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=r=0
        a=[]
        nums1.sort()
        nums2.sort()
        while l<len(nums1) and r<len(nums2):
            if nums1[l]==nums2[r]:
                a.append(nums1[l])
                l+=1
                r+=1
            elif nums1[l]>nums2[r]:
                r+=1
            else:
                l+=1
        #print(a)
        return set(a)
        #return set(nums1).intersection(nums2)
