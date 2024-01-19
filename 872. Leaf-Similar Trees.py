#872. Leaf-Similar Trees
#https://leetcode.com/problems/leaf-similar-trees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ary1=[]
        ary2=[]

        def outAry(root,ary):
            
            if root.left is not None:
                outAry(root.left,ary)
            if root.right is not None:
                outAry(root.right,ary)
            if root.left is None and root.right is None:
                ary.append(root.val)
            return ary
        ary1=outAry(root1,ary1)
        ary2=outAry(root2,ary2)
        #print(ary1)
        #print(ary2)
        if ary1==ary2:
            return True
        else:
            return False
