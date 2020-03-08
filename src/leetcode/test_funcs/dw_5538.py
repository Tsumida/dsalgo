# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            # 0 for left, 1 for right
            if not node:
                return (-1, -1)
            else:
                a, b = dfs(node.left)
                c, d = dfs(node.right)
                l_v = b + 1
                r_v = c + 1
                nonlocal res
                res = max(res, l_v, r_v)
                print(res)
                return (l_v, r_v)
        res = 0
        if root and not root.left and not root.right:
            dfs(root)
        return res

