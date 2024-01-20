#931. Minimum Falling Path Sum
#https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        x=len(matrix[0])
        y=len(matrix)
        if y==1:
            return min(matrix[0])
        z=[[100000]*x for _ in range(y)]
        for j in range(x):
            z[0][j]=matrix[0][j]
        for i in range(1,y):
            for j in range(x):
                a,b,c=j-1,j,j+1
                if a<0:
                    a=0
                if c>=x:
                    c=x-1
                for k in {a,b,c}:
                    if z[i][j]> z[i-1][k]+matrix[i][j]:
                        z[i][j]=min(z[i][j],z[i-1][k]+matrix[i][j])
        return min(z[y-1])
    
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        x=len(matrix[0])
        y=len(matrix)
        if y==1:
            return min(matrix[0])
        z=[[100000]*x for _ in range(y)]
        for j in range(x):
            z[0][j]=matrix[0][j]
        for i in range(1,y):
            for j in range(x):
                a,b,c=j-1,j,j+1
                if a<0:
                    a=0
                if c>=x:
                    c=x-1
                z[i][j]=min(z[i][j],z[i-1][a]+matrix[i][j],z[i-1][b]+matrix[i][j],z[i-1][c]+matrix[i][j])
        return min(z[y-1])