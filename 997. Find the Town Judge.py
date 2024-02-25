#997. Find the Town Judge
#https://leetcode.com/problems/find-the-town-judge/description/?envType=daily-question&envId=2024-02-22

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        jud=[i for i in range(1,n+1)]
        cntjud = defaultdict(int)
        for a in trust:
            if a[0] in jud:
                jud.remove(a[0])
            cntjud[a[1]]+=1
        #print(cntjud,jud[-1],cntjud[jud[-1]],n)
        if not len(jud)==0:
            if cntjud[jud[-1]]==n-1:
                return jud[-1]
        return -1
    


#may consider use DP .. list to fill the number