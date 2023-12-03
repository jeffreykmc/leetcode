#1266. Minimum Time Visiting All Points


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x=0
        dist=0
        pastX=0
        pastY=0
        for p in points:
            if x==0:
                pastX,pastY=p
            else:
                thisX,thisY=p
                if abs(thisX-pastX) > abs(thisY-pastY):
                    dist+=abs(thisX-pastX)
                else:
                    dist+=abs(thisY-pastY)
                #print(dist)
                pastX=thisX
                pastY=thisY
            x=1
        return dist

        