#3005. Count Elements With Maximum Frequency
#https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        deN=defaultdict(int)
        
        for a in nums:
            if a not in deN:
                deN[a]=nums.count(a)

        
        thisCount=thisMax=0
        #print(sorted(deN.items()))
        #for a,b in sorted(deN.items()):
        for a in sorted(deN, key=deN.get, reverse=True):   
            if thisMax==0:
                #print('Max0',a,deN[a],thisMax,thisCount)
                thisMax=deN[a]
                thisCount+=deN[a]
            elif thisMax==deN[a]:
                #print('Max1',a,deN[a],thisMax,thisCount)
                thisCount+=deN[a]
            else:
                #print('Max#',a,deN[a],thisMax,thisCount)
                break
        return thisCount