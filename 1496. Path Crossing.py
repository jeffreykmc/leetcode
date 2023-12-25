#1496. Path Crossing
#https://leetcode.com/problems/path-crossing/description/?envType=daily-question&envId=2023-12-23

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x=0
        y=0
        trail=['000000']
        for a in path:
            if a=="N":
                y+=1
            if a=="S":
                y-=1
            if a=="E":
                x+=1
            if a=="W":
                x-=1
            here='{:03d}'.format(x)+'{:03d}'.format(y)
            if here in trail:
                return True
            trail.append(here)
        return False

            