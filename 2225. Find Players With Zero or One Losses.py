#2225. Find Players With Zero or One Losses
#https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/?envType=daily-question&envId=2024-01-15

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a=[[],[]]
 #       a[0]=[]
 #       a[1]=[]
        win={}
        lost={}

        for m in matches:
            try:
                win[m[0]]+=1
            except:
                #print(m[0])
                win[m[0]]=1
            try:
                lost[m[1]]+=1
            except:
                lost[m[1]]=1
        for w in win:
            if w not in lost:
                #print(w)
                a[0].append(w)
        for l in lost:
            if lost[l]==1:
                a[1].append(l)
        a[0].sort()
        a[1].sort()
        return a
