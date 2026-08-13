# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, highest):
            if not node: return 0

            res = 1 if node.val >= highest else 0
            highest = max(highest, node.val)
            res += dfs(node.left, highest)
            res += dfs(node.right, highest)
            return res
        return dfs(root, root.val)

