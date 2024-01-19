#1235. Maximum Profit in Job Scheduling
#https://leetcode.com/problems/maximum-profit-in-job-scheduling/








#time exceeded
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #https://www.techiedelight.com/weighted-interval-scheduling-problem/
        #https://www.techiedelight.com/activity-selection-problem/

        #https://stackoverflow.com/questions/63131071/how-to-only-update-list-within-list-based-on-index-in-python-without-updating-a
        #ab=[[0,0,0]]*len(startTime)

        def findLastNonConflictingJob(jobs: List[int],n:int):
            for i in reversed(range(n)):
                if jobs[i][1] <= jobs[n][0]:
                    return i
            # return the negative index if no non-conflicting job is found
            return -1
            
        def findMaxProfit(jobs: List[int],n:int):
            # base case
            if n < 0:
  #              print('fMP',n,-1)
                return 0
            # return if only one item is remaining
            if n == 0:
 #               print('fMP+',n,jobs[0][2])
                return jobs[0][2]
            # find the index of the last non-conflicting job with the current job
            index=findLastNonConflictingJob(jobs, n)
            # include the current job and recur for non-conflicting jobs `[0, index]`
            incl = jobs[n][2] + findMaxProfit(jobs, index)
            # exclude the current job and recur for remaining items `[0, n-1]`
            excl = findMaxProfit(jobs, n-1)
            # return the maximum profit by including or excluding the current job
            return max(incl, excl)

        islot=len(startTime)
        ab=[[0,0,0].copy() for _ in range(islot)]
#        maxP=[0]*islot
#        print(ab)
        for i in range(islot):
            ab[i][0]=startTime[i]
            ab[i][1]=endTime[i]
            ab[i][2]=profit[i]
#            print(i,ab[i])
        ab.sort(key=lambda x:(x[1]))

 #       print(ab)
        return findMaxProfit(ab, len(ab) - 1);


