#2108. Find First Palindromic String in the Array
#https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=daily-question&envId=2024-02-13

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for w in words:
            i=len(w)
            gotit=True
            for a in range(i//2):
                if w[a]!=w[i-a-1]:
                    gotit=False
                    break
            if gotit:
                return w
        return ""
            
#class Solution:
#    def firstPalindrome(self, words: List[str]) -> str:
#        words.append("")
#        for word in words:
#            if word == word[::-1]:
#                return word