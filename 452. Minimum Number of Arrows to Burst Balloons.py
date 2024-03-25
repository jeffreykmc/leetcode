#452. Minimum Number of Arrows to Burst Balloons
#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=daily-question&envId=2024-03-18

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        aout=[]
        for x,y in sorted(points):
            checked=False
            for i in range(len(aout)):
                #print(aout)
                if (x>=aout[i][0] and x<=aout[i][1]) or (y>=aout[i][0] and y<=aout[i][1]):
                    aout[i][0]=max(aout[i][0],x)
                    aout[i][1]=min(aout[i][1],y)
                    checked=True
            if not checked:
                aout.append([x,y])

        return len(aout)


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        prev = 0
        arrows = 1

        for i in range(1, len(points)):
            if points[i][0] > points[prev][1]:
                arrows += 1
                prev = i

        return arrows