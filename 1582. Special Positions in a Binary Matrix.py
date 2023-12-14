#1582. Special Positions in a Binary Matrix
#https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/?envType=daily-question&envId=2023-12-13

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        dmat=mat
        totalcount=0
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                if mat[j][i]==1:
                    sumx=0
                    sumy=0
                    
                    for x in range(len(mat)):
                        sumx+=mat[x][i]
                    for y in range(len(mat[0])):
                        sumy+=mat[j][y]
                    if sumx==1 and sumy==1:
                        totalcount+=1
        return totalcount


