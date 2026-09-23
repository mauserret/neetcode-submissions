# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        pre_iter = iter(preorder)

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_num = next(pre_iter)
            root = TreeNode(root_num)
            mid = inorder_idx[root_num]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)