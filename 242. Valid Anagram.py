#242. Valid Anagram
#https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v=t
        i=0
        while i<len(s):
            if len(v)==0:
                return False
            if s[i] in v:
                v=v.replace(s[i],"",1)
            i=i+1
        return True


#string replacement method
    def method1()
        v=t
        i=0
        while i<len(s):
            if len(v)==0:
                return False
            if s[i] in v:
                v=v.replace(s[i],"",1)
            i=i+1
        if len(v)==0:
            return True
        else:
            return False
        


    def method2()
        v=s
        if len(v)==1 or len(t)==1:
            if t in s:
                return True
            else:
                return False
        
        for i in range(0,len(t)-1):
            
            if t[i] in v:
                v=v.replace(t[i],'_',1)
            else:
                return False
        return True