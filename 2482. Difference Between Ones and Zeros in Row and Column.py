#2482. Difference Between Ones and Zeros in Row and Column
#https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        #https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/solutions/4401899/beats-100-explained-with-video-count-row-and-column-1s-c-java-python-js-visualized/
        m=len(grid)
        n=len(grid[0])
        dmat=[[0 for j in range(n)] for i in range(m)]
        
        row_ones = [0] * m
        col_ones = [0] * n

        # Count ones in each row and column
        for i in range(m):
            for j in range(n):
                row_ones[i] += grid[i][j]
                col_ones[j] += grid[i][j]

        # Calculate the difference matrix
        for i in range(m):
            for j in range(n):
                dmat[i][j] = 2 * (row_ones[i] + col_ones[j]) - m - n

        return dmat

#       following is my work but the problem is time limit exceeded
#        for i in range(n):
#            for j in range(m):
#                sumx=0
#                sumy=0
#                for x in range(n):
#                    if grid[x][i]==1:
#                        sumx+=1
#                    else:
#                        sumx-=1
#                for y in range(m):
#                    if grid[j][y]==1:
#                        sumy+=1
#                    else:
#                        sumy-=1        
#                dmat[j][i]=sumx+sumy
#        return dmat


