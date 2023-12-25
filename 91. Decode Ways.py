#91. Decode Ways
#https://leetcode.com/problems/decode-ways/?envType=daily-question&envId=2023-12-25


class Solution:
    def numDecodings(self, s: str) -> int:
        count=0
        sdict={
            '01':1,
            '02':1,
            '03':1,
            '04':1,
            '05':1,
            '06':1,
            '07':1,
            '08':1,
            '09':1,
            '10':1,
            '11':2,
            '12':2,
            '13':2,
            '14':2,
            '15':2,
            '16':2,
            '17':2,
            '18':2,
            '19':2,
            '20':1,
            '21':2,
            '22':2,
            '23':2,
            '24':2,
            '25':2,
            '26':2            
        }

        if len(s)==2:
            if s[:1]=='0':
                return 0
            if s in sdict:
                return sdict[s]
            else:
                return 1
        if len(s)==1:
            if s=='0':
                return 0
        r=len(s)
        for i in range(0,r,2):
            thisS=s[i:i+2]           
            if thisS in sdict:
                count+=sdict[thisS]
            else:
                if len(thisS)==1:
                    count+=1
                else:
                    count+=2
        return count

