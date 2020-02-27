# Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def method_recur(pl:int, pr:int, il:int, ir:int):
            # l, r is the interval in preorder seq.
            n = pr-pl
            assert n == ir - il
            if n == 0:
                return None
            elif n == 1:
                return TreeNode(preorder[pl])
            delta = inorder[il:ir].index(preorder[pl]) # 相对偏移
            left = method_recur(pl+1, pl+1+delta, il, il+delta)
            right = method_recur(pl+1+delta, pr, il+delta+1, ir)
            ro = TreeNode(preorder[pl])
            ro.left = left
            ro.right = right
            return ro

        n = len(preorder)
        assert n == len(inorder)
        return method_recur(0, n, 0, n)


