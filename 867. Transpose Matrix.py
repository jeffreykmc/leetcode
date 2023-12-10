#867. Transpose Matrix
#https://leetcode.com/problems/transpose-matrix/


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #https://www.programiz.com/python-programming/examples/transpose-matrix
        #https://leetcode.com/problems/transpose-matrix/solutions/4384180/video-give-me-5-minutes-2-solutions-how-we-think-about-a-solution/?envType=daily-question&envId=2023-12-10
        
        new=[[0] * len(matrix) for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new[j][i]=matrix[i][j]
        #print(new)
        return new
