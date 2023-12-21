#1637. Widest Vertical Area Between Two Points Containing No Points
#https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/



class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        spoints=sorted(points,key=lambda x: x[0],reverse=True)
        maxW=0
        for p in range(1,len(points)):
            if abs(spoints[p][0]-spoints[p-1][0]) > maxW:
                maxW=abs(spoints[p][0]-spoints[p-1][0])
        return maxW