# 2019-7-16

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def max_depth(r:TreeNode, r_dep:int) -> int:
            # next level -> fa_dep + 1
            if r == None:
                return r_dep

            left_max_dep  = max_depth(r.left, r_dep+1)
            right_max_dep = max_depth(r.right, r_dep+1)

            return  max(left_max_dep, right_max_dep)

        def process(r:TreeNode, r_dep:int) -> (TreeNode, int):

            if r == None \
                or r.left == None     \
                and r.right == None \
                and r_dep == maxdepth - 1:

                print(r.val, r_dep)
                return (r, r_dep)

            this_prec = None
            this_max_dep = r_dep
            left_prec, dl = process(r.left, r_dep + 1)
            right_prec, dr = process(r.right, r_dep + 1)

            if left_prec != None and right_prec != None:
                this_prec, this_max_dep = r, r_dep
            elif left_prec == None:
                this_prec, this_max_dep = right_prec, dr
            else:
                this_prec, this_max_dep = left_prec, dl

            #print("r={}, r_dep={}, this_max_dep={}, this_prec={}".format(r.val, r_dep, this_max_dep, this_prec.val))

            return (this_prec, this_max_dep)

        # O(n)
        maxdepth = max_depth(root, 0)
        prec, max_dep = process(root, 0)

        print("mdp={}, prec={}, {}".format(maxdepth, prec.val, max_dep))

        return prec
