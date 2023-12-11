#1287. Element Appearing More Than 25% In Sorted Array
#https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/?envType=daily-question&envId=2023-12-11


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        b={}
        maxA=0
        maxB=0
        for a in arr:
            try:
                b[a]+=1
            except:
                b[a]=1
            if b[a]>maxB:
                maxB=b[a]
                maxA=a
        return maxA

        