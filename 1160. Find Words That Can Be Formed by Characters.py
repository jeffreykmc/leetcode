#1160. Find Words That Can Be Formed by Characters
#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=0
        for w in words:
            thisS=chars
            c=0
            for a in w:
                if a in thisS:
                    thisS=thisS.replace(a,'_',1)
                    c+=1
                else:
                    break
            if c==len(w):
                count+=len(w)
        return count
