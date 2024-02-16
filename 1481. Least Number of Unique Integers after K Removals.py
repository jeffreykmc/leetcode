#1481. Least Number of Unique Integers after K Removals
#https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=daily-question&envId=2024-02-16


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        #sortarr=sorted(arr,key=arr.count,reverse=False)
        sortarr=list(chain.from_iterable(repeat(i,c) for i,c in Counter(arr).most_common()))
        #https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/

        #print(sortarr)
        for i in range(k):
            sortarr.pop()
        #print(sortarr)
        return (len(Counter(sortarr)))

