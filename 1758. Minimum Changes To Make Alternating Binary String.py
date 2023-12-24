#1758. Minimum Changes To Make Alternating Binary String
#https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/?envType=daily-question&envId=2023-12-24
#

class Solution:
    def minOperations(self, s: str) -> int:

        count01=0
        count10=0
        #010101010
        thisA='0'
        thisB='1'
        for a in s:
            if a!=thisA:
                count01+=1
            if a!=thisB:
                count10+=1
            thisA,thisB=thisB,thisA
        return(min(count01,count10))
    
    

class Solution1:
    def minOperations(self, s: str) -> int:

        #010101010

        r=len(s)
        if r==1:
            return 0
        if r==2:
            if s.count('0')==0 or s.count('0')==2:
                return 2
            else:
                return 0
        #return r

        #101010101
        count10=0
        count01=0
        count00=0
        count11=0
        if r%2==1:
            if s[:1]!=s[-1:]:
                count10+=1
                count01+=1

        for i in range(0,r,2):
            thisS=s[i:i+2]
            if thisS=='10':
                count10+=1
            if thisS=='01':
                count01+=1
            if thisS=='00':
                count00+=1
            if thisS=='11':
                count11+=1

            print("*",count10+count11+count10,count01+count11+count10)
        return(min(count10+count11+count10,count01+count11+count10))
