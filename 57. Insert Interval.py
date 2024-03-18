#57. Insert Interval
#https://leetcode.com/problems/insert-interval/description/?envType=daily-question&envId=2024-03-17

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        start, end = newInterval
        
        inserted = False
        for inv in intervals:
            cstart, cend = inv
            
            if cend < start or inserted:
                ans.append([cstart, cend])
                continue
            
            start = min(start, cstart)
            if end < cstart:
                ans.append([start, end])
                ans.append([cstart, cend])
                inserted = True
                continue
            
            if end <= cend:
                ans.append([start, cend])
                inserted = True
        
        if not inserted:
            ans.append([start, end])
        
        return ans
    

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a=set()
        out=[]
        print(a)
        for inter in intervals:
            for i in range(inter[0],inter[1]+1):
                a.add(i)
        for i in range(newInterval[0],newInterval[1]+1):
            a.add(i)
        #create set
        thisIn=0
        thisOut=0
        this=-2
        for thisa in a:
            
            if thisa==this+1:
                print('this',this,thisIn,thisOut,thisa)
                this+=1
            elif thisIn==0:
                print('thisIn',this,thisIn,thisOut,thisa)
                thisIn=thisa
                this=thisa
            else:
                print('thisOut',this,thisIn,thisOut,thisa)
                out.append([thisIn,thisa])
                this=-2
            #print(thisa)
        out.append([thisIn,thisa])
        print(out)
        return out
