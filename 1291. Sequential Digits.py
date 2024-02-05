#1291. Sequential Digits
#https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2024-02-02

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        a=[]
        for i in range(len(str(low)),len(str(high))+1):
            for j in range(9-i+1):
                if j+i<=9:
                    this=int(s[j:j+i])
                    if this>=low and this<=high:
                        a.append(this)
        return a
