#938. Range Sum of BST
#https://leetcode.com/problems/range-sum-of-bst/description/?envType=daily-question&envId=2024-01-08

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def returnVal(root,low,high):
            rval=lval=0
            if root.left is not None:
                lval=returnVal(root.left,low,high)
            if root.right is not None:
                rval=returnVal(root.right,low,high)
            if root.val>=low and root.val<=high:
                return root.val+rval+lval
            else:
                return rval+lval
        return returnVal(root,low,high)