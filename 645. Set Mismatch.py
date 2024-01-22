#645. Set Mismatch
#https://leetcode.com/problems/set-mismatch/description/?source=submission-noac

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:


#https://leetcode.com/problems/set-mismatch/description/comments/2221916
#some one use mathematic summarization to find the missing and duplicate one.
        
        
        
        
        
        
        
        
        
        
        
        
        s={}
        b=[]
        missing=-1
        duplicate=-1
        x=1
        for a in nums:
            if x not in nums:
                missing=x
            if a not in s:
                s[a]=1
            else:
                duplicate=a
            if missing !=-1 and duplicate!=-1:
                b.append(duplicate)
                b.append(missing)
                #print('break',x,a,missing,duplicate)
                break
            #print('cont ',x,a,missing,duplicate)
            x+=1

        return b        
        #nums.sort()
        x=1

        for i in nums:

            if i!=x:
                if x not in nums:
                    s.append(i) 
                    s.append(x)
            x+=1
        return s
