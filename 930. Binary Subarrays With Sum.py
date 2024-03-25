#930. Binary Subarrays With Sum
#https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-14


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        cnt=0
        if goal>0:
            a=goal
        else:
            a=1
        for w in range(a,n+1): #slinding windows
            b=0
            for i in range(n-w+1): #start of slind windows
                if b==0:
                    thisS=sum(nums[i:i+w])
                    #print(b,n,i,i+w,thisS)
                    b=1
                else:
                    thisS=thisS-nums[i-1]+nums[i+w-1]
                    #print(b,n,i,i+w,thisS)
                if thisS==goal:
                    cnt+=1
                
        return cnt




