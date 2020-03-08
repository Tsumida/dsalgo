# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 还没passed
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (int, bool, int, int):
            if not node:
                return 0, True, 10000000, -10000000
            else:
                a, b, lmin, lmax = dfs(node.left)
                c, d, rmin, rmax = dfs(node.right)
                val = node.val
                is_a_bst = b and d
                self_min, self_max = 10000000, -10000000
                if node.left:
                    is_a_bst = is_a_bst and node.left.val < lmax and lmax < val and node.left.val < val
                    self_min = lmin
                if node.right:
                    is_a_bst = is_a_bst and val < rmin and rmin < node.right.val and node.right.val > val
                    self_max = rmax

                if abs(self_min) == 10000000:
                    self_min = node.val
                if abs(self_max) == 10000000:
                    self_max = node.val

                self_val = val + a + c
                self_is_bst = is_a_bst
                if self_is_bst:
                    nonlocal res
                    res = max(res, self_val)
                print(self_val, self_is_bst, self_min, self_max)
                return self_val, self_is_bst, self_min, self_max


        res = 0
        if root:
            dfs(root)
        return res
