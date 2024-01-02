#2610. Convert an Array Into a 2D Array With Conditions
#https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        outx=[[]]
        for x in nums:
            outi=0
            try:
                while x in outx[outi]:
                    outi+=1
                outx[outi].append(x)
            except:
                outx.append([x])
        return outx