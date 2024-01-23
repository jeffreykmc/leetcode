#2125. Number of Laser Beams in a Bank
#https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-03

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        sbank=[]
        totalBean=0
        thisBean=0
        preBean=0
        for x in range(len(bank)):
            thisBean=bank[x].count('1')
            if thisBean>0:               
                totalBean+=thisBean*preBean
                preBean=thisBean
#            sbank.append(bank[x].count('1'))
            
#        print(bank)
#        print(sbank)
        return totalBean

