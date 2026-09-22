# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        def dfs(node, vals):
            if not node: return

            dfs(node.left, vals)
            vals.append(node.val)
            dfs(node.right, vals)
        dfs(root, vals)

        return vals[k - 1]

