#111. Minimum Depth of Binary Tree
#https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#https://leetcode.com/problems/minimum-depth-of-binary-tree/solutions/3413009/5-lines-recursive-solution-python/
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left: 
            return 1+self.minDepth(root.right)
        elif not root.right:
            return 1+self.minDepth(root.left)
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
