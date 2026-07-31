# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            maxRight = self.maxDepth(root.right)
            maxLeft = self.maxDepth(root.left)
            return max(maxRight, maxLeft) + 1

        