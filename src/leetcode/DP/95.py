# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree2list(root: TreeNode) -> list:
    def dfs(r: TreeNode):
        if r:
            dfs(r.left)
            res.append(r.val)
            dfs(r.right)
        #else:
        #   res.append(-1)


    res = []
    dfs(root)
    return res


'''
给定n, 生成所有有n个结点的BST
'''

class Solution:

    def generateTrees(self, n: int) -> list:

        def add_val(r: TreeNode, val: int):
            if r:
                r.val += val
                add_val(r.left, val)
                add_val(r.right, val)

        def copy_tree(r: TreeNode):
            if not r:
                return None
            else:
                left = copy_tree(r.left)
                right = copy_tree(r.right)
                new_root = TreeNode(r.val)
                new_root.left = left
                new_root.right = right
                return new_root


        if n == 0:
            return []
        elif n == 1:
            return [TreeNode(1)]
        else:
            result = [[None], [TreeNode(1)]]
            # 从 f(0), ..., f(i-1)计算f(i)
            for i in range(2, n+1):
                tmp = list()    # 存放临时结果
                for k in range(1, i+1):
                    # f(k) X f(n-k-1), 后者的val要加上 k
                    for left in result[k-1]:
                        for right in result[i-k]:
                            r = TreeNode(k)
                            r.left = copy_tree(left)
                            r.right = copy_tree(right)
                            add_val(r.right, k)
                            tmp.append(r)

                result.append(tmp)
            #for i, t in enumerate(result):
            #    for tree in t:
            #       print("-"*3, tree2list(tree))

            return result[-1]

s = Solution()
# 0 --> empty
# 1 --> 1
# 2 --> 2
# 3 --> 5
#
r1 = s.generateTrees(n=3) # 5种
print(f"r1.len() = {len(r1)}\n", "\n".join(str(tree2list(r)) for r in r1))
