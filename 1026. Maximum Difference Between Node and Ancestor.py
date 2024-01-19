#1026. Maximum Difference Between Node and Ancestor
#https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/?envType=daily-question&envId=2024-01-11


#fail


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rMin(root):
            a=1000000
            if root is None:
                return a
            if root.left is not None:
                #print('rMin+',root.val,root.left.val)
                a=min(rMin(root.left),root.val,root.left.val,a)
            if root.right is not None:
                #print('rMin-',root.val,root.right.val)
                a=min(rMin(root.right),root.val,root.right.val,a)
            #print('rMin',root.val,a,min(a,root.val))
            return min(a,root.val)
        

        def rMax(root):
            a=0
            if root is None:
                return a
            if root.left is not None:
                #print('rMax+',root.val,root.left.val)
                a=max(rMax(root.left),root.val,root.left.val,a)
            if root.right is not None:
                #print('rMax-',root.val,root.right.val)
                a=max(rMax(root.right),root.val,root.right.val,a)
            #print('rMax',a)
            return max(a,root.val)

        #print(rMin(root.left))
        #print(rMin(root.right))
        #print(rMax(root.left))
        #print(rMax(root.right))
        
        #print(root.val,rMax(root.left),rMin(root.left))
        #print(root.val,rMax(root.right),rMin(root.right))
        return max(max(root.val,rMax(root.left))-min(root.val,rMin(root.left)) ,max(root.val,rMax(root.right))-min(root.val,rMin(root.right)))