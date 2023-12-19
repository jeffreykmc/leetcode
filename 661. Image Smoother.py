#661. Image Smoother
#https://leetcode.com/problems/image-smoother/description/?envType=daily-question&envId=2023-12-19

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        #https://stackoverflow.com/questions/45765223/update-value-in-multidimensional-list-in-python
        w=len(img[0])
        h=len(img)
        simg=[[0 for x in range(w)] for y in range(h)]
        for j in range(h):
            for i in range(w):
                a=0
                count=0
                #https://leetcode.com/problems/image-smoother/solutions/4423065/96-31-easy-solution-with-explanation/?envType=daily-question&envId=2023-12-19
                #for x in range(max(0, i-1), min(rows, i+2)):
                #for y in range(max(0, j-1), min(cols, j+2)):
                for k in range(-1,2):
                    for l in range(-1,2):
                        if j+k>=0 and j+k<h and i+l>=0 and i+l<w: 
                            a+=img[j+k][i+l]   
                            count+=1
                simg[j][i]=floor(a/count)
        return simg