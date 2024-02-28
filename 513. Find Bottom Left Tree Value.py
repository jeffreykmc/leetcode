#513. Find Bottom Left Tree Value
#https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=daily-question&envId=2024-02-28

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        a=[]
        def returnleft(root,lv,a):
            if root is None:
                return a
            a.append([lv,root.val])
            a=returnleft(root.left,lv*10+1,a)
            a=returnleft(root.right,lv*10+2,a)
            return a
        a=returnleft(root,1,a)
        #print(a)
        maxb=1
        minc=a[0][1]
        
        for b,c in a:
            #print(b,c,len(str(b)),len(str(maxb)))
            if len(str(b))-len(str(maxb))>=1:
                maxb=b
                minc=c
            elif len(str(b))==len(str(maxb)):
                if b<maxb:
                    minc=c
        return minc
    

#https://leetcode.com/problems/find-bottom-left-tree-value/solutions/4792343/easy-solution-in-c-python-java-javascript-with-explanation/?envType=daily-question&envId=2024-02-28
    
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = deque([root])
        leftmost = None

        while queue:
            leftmost = queue.popleft()

            if leftmost.right:
                queue.append(leftmost.right)
            if leftmost.left:
                queue.append(leftmost.left)

        return leftmost.val
    
