#1436. Destination City
#https://leetcode.com/problems/destination-city/description/?envType=daily-question&envId=2023-12-15


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityDic={}
        startCity=paths[0][0]
        for a,b in paths:
            #1.1 as it is a start city. add more weight to that city
            try:
                cityDic[a]+=1.1
            except:
                cityDic[a]=1.1
            try:
                cityDic[b]+=1
            except:
                cityDic[b]=1
    
        for a in cityDic:
            if cityDic[a]==1 and a!=startCity:
                #print({k: v for k, v in sorted(cityDic.items(), key=lambda item: item[1])})
                return a
        return ""