#1704. Determine if String Halves Are Alike
#https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiou'
        # Splitting string using string slicing
        n = len(s)
        if n%2 == 0:
            s1=s[0:n//2]
            s2=s[n//2:]
        else:
            s1=s[0:(n//2+1)]
            s2=s[(n//2+1):]
        tc1=tc2=0
        for v in vowels :
            tc1+=s1.lower().count(v)
            tc2+=s2.lower().count(v)
        
        if tc1==tc2:
            return True
        else:
            return False
        
