#49. Group Anagrams
#https://leetcode.com/problems/group-anagrams/description/?envType=daily-question&envId=2024-02-06



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        vout=[]
        def thisC(strA):
            i=0
            for a in strA:
                i+=100**(ord(a)-ord('a'))
            return i
        
        for thisS in strs:
            thisI=thisC(thisS)
            if thisI not in vout:
                vout.append(thisI)
                out.append([thisS])
            else:
                out[vout.index(thisI)].append(thisS)
        return out



#use the wording list hash map
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = {}
        
        for x in strs:
            s_w = ''.join(sorted(x))
            if s_w not in li:
                li[s_w]=[x]
            else:
                li[s_w].append(x)
        
        return list(li.values())
        
