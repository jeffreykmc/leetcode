#2149. Rearrange Array Elements by Sign
#https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        out=[]
        
        for a in nums:
            if a > 0:
                pos.append(a)
            else:
                neg.append(a)
        for i in range(len(nums)//2):
            out.append(pos[i])
            out.append(neg[i])
        return out
                


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        i_pos, i_neg = 0, 1
        for num in nums:
            if num > 0:
                i = i_pos
                i_pos += 2
            else:
                i = i_neg
                i_neg += 2

            result[i] = num
        
        return result
