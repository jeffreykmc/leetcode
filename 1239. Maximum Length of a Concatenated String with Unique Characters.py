#1239. Maximum Length of a Concatenated String with Unique Characters
#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23


# fail


from itertools import combinations

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        comarr=[]
        jcomarr=[]
        for n in range(len(arr)+1):
            comarr+=list(combinations(arr,n))
        for a in comarr:
            jcomarr.append(''.join(a))
        kcomarr=jcomarr.copy()
        for a in jcomarr:


            skip=False
            #b=''.join(a)
            print('a',a)
            for c in arr:
                if c in a:
                    d=a.replace(c,'')
                    print('[check] ',a,'/',d,' by ',c)
                    for k in range(len(c)):
                        #print('check',a,d,'by',c,'-',k,c[k])
                        if c[k] in d:
                            kcomarr.remove(a)
                            skip=True
                            print('##Fail Remove## ',a)
                        if skip:
                            break
                    
                    if skip:
                        break
                    else:
                        print('##Keep it##',a)
        maxL=0
        print(kcomarr)
        for a in kcomarr:
            print(maxL,a,len(a))
            maxL=max(maxL,len(a))
        return maxL
