#387. First Unique Character in a String

#https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=daily-question&envId=2024-02-05

class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos=-1
        for t in s:
            pos+=1
            if s.count(t)==1:
                return pos
        return -1