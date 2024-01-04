#455. Assign Cookies
#https://leetcode.com/problems/assign-cookies/description/?envType=daily-question&envId=2024-01-01



class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        #https://leetcode.com/problems/assign-cookies/solutions/4485003/approach-explained/?envType=daily-question&envId=2024-01-01

        g.sort(reverse = True)
        s.sort(reverse = True)
        res, i , j = 0 ,0,0
        print(g)
        print(s)
        print('00000000000')
        while i<len(g) and j<len(s):
            
            if g[i]<=s[j]:
                print('add res',res,i,j,g[i],s[j])
                res+=1
                i+=1
                j+=1
            else:
                print('skip',res,i,j,g[i],s[j])
                
                i+=1
        return res
    


#my very beginning design is thinking teh size should be excat greed to the child

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cg=Counter(g)
        cs=Counter(s)
        totalcount=0
        for a,b in cs.items():
            if a in cg:
                thisc=cg[a]  
                if thisc>b:
                    totalcount+=b
                elif b>=thisc:
                    totalcount+=thisc
        return totalcount
    
