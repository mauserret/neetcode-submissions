# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        string = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                string.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                string.append("null")
        return ",".join(string)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            node = queue.popleft()

            if values[index] != "null":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            if index < len(values) and values[index] != "null":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root


