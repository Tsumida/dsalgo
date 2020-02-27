# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree2list(root: TreeNode) -> list:
    def inorder(subroot: TreeNode):
        if subroot:
            inorder(subroot.left)
            res.append(subroot.val)
            inorder(subroot.right)

    res = list()
    inorder(root)
    return res


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> list:
        def tree_sum(r: TreeNode) -> int:
            if r:
                left_sum = tree_sum(r.left)
                right_sum = tree_sum(r.right)
                r_sum: int = r.val + left_sum + right_sum

                table[r_sum] = table.get(r_sum, 0) + 1

                return r_sum
            else:
                return 0

        table = dict()
        if root:
            _ = tree_sum(root)
            max_sum = max(table.values())
            print(table.items())
            return [ k for k, v in table.items() if v == max_sum]
        else:
            return []
# consider: zero, positive, negative


s = Solution()
r_1 = TreeNode(x=5)
r_1.left = TreeNode(x=2)
r_1.right = TreeNode(x=-3)
print(s.findFrequentTreeSum(root=r_1)) # [2, -3, 4]

r_2 = TreeNode(x=5)
r_2.left = TreeNode(x=2)
r_2.right = TreeNode(x=-5)
print(s.findFrequentTreeSum(root=r_2)) #[2]

r_2 = TreeNode(x=1)
r_2.left = TreeNode(x=2)
r_2.right = TreeNode(x=3)
print(s.findFrequentTreeSum(root=r_2)) # [2, 3, 6]

print(s.findFrequentTreeSum(root=None))
