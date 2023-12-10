#1716. Calculate Money in Leetcode Bank

class Solution:
    def totalMoney(self, n: int) -> int:
        savewk=0
        saveday=1
        save=0
        for i in range(1,n+1):
            save+=saveday+savewk
            saveday+=1
            print(i,savewk,save)
            if i%7==0:
                savewk+=1
                saveday=1
        return save
