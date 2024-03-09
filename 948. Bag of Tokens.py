#948. Bag of Tokens
#https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04

class Solution:
#https://leetcode.com/problems/bag-of-tokens/solutions/4818912/beat-100-00-full-explanation-with-pictures/?envType=daily-question&envId=2024-03-04
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        max_score = 0
        left = 0
        right = n - 1
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
                
        return max_score
