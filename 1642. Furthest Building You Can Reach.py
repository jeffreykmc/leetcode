#1642. Furthest Building You Can Reach
#https://leetcode.com/problems/furthest-building-you-can-reach/description/?envType=daily-question&envId=2024-02-17













#Fail




class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        bricksused=0
        laddersused=0
        lad=[]
        dp=[0 for x in range(len(heights))]
        dp1=[0 for x in range(len(heights))]
        #print(dp,dp1)
        if len(heights)==2:
            if bricks==0 and ladders==0:
                return 0
        for x in range(2,len(heights)):
            if heights[x]>heights[x-1]:
                dp[x]=heights[x]-heights[x-1]
                #any ladder left? use ladder first
                if laddersused<ladders:
                    laddersused+=1
                    print('l',x,laddersused,dp,lad)
                else:
                    #replace the leased by brick
                    if laddersused>0:
                        if dp[x]>lad[-1]:
                            #replace brick can't fill the gap
                            print('nouse',x,dp[x],lad[-1],laddersused,bricksused,dp,lad)
                            return x
                        thisbrick=lad.pop(len(lad)-1)
                        if thisbrick+bricksused>bricks:
                            #not enough brick
                            print('nobrick',x,dp[x],laddersused,bricksused,thisbrick,dp,lad)
                            return x-1
                        else:
                            bricksused+=thisbrick
                            laddersused-=1
                            print('replace',x,dp[x],laddersused,bricksused,thisbrick,dp,lad)
                    else:
                        if dp[x]+bricksused>bricks:
                            print('nobrick&noladder',x,dp[x],laddersused,bricksused,dp,lad)
                            return x-1
                    print('b',x,laddersused,dp,lad)
                a=0
                while a<len(lad):
                    if dp[lad[a]]<dp[x]:
                        break
                    a+=1
                #print('lad-append',a,x,lad)
                lad.insert(a,x)
        return len(heights)

'''
                if len(lad)<=1:
                    lad.append(x)
                else:
                    while dp[lad[a]]<dp[x] and a<len(lad):
                        a+=1
                    lad.append(a,x)
'''


        