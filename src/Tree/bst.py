# 2020-01-17
from typing import List


class BinarySearchTree:
    class Node:
        def __init__(self, val:int, left=None, right=None, father=None):
            self.val = val
            self.left = left
            self.right = right
            self.father = father

        def __eq__(self, other):
            if self and other:
                return id(self) == id(other)
            elif not self and not self:
                return True
            else:
                return False


        def __str__(self):
            # 不要打印self.father, 因为它默认用前序遍历导致无限递归
            return "({}, {}, {})".format(self.val, id(self.left.val), id(self.right.val))

    def __init__(self):
        self.root = None

    def inorder_seq(self) -> List[int]:
        def recur(r:BinarySearchTree.Node, lis:List[int]):
            if r:
                recur(r.left, lis)
                lis.append(r.val)
                recur(r.right, lis)

        res = list()
        recur(self.root, res)
        return res

    def search(self, val:int) -> Node:
        # may return None
        p = self.root
        while p:
            if p.val == val:
                break
            elif p.val <= val:
                p = p.right
            else:
                p = p.left
        return p # may be None.

    def is_bst(self) -> bool:
        # 语义: t是BST <=>
        #    (None, None) <=> t.root == None
        # 或 (l, r) && l.val <= t.val <= r.val
        # 递归判断 max(r.left).val <= r.val <= min(r.right).val
        def recur(r:BinarySearchTree.Node):
            if not r:
                return (None, None, True)
            else:
                l_min, l_max, lb = recur(r.left)
                r_min, r_max, rb = recur(r.right)
                if not l_max:
                    l_max = r
                if not l_min:
                    l_min = l_max
                if not r_min:
                    r_min = r
                if not r_max:
                    r_max = r_min
                if lb & rb and l_max.val <= r.val and r.val <= r_min.val:
                    return (l_min, r_max, True)
                else:
                    return (None, None, False)

        if not self.root:
            return True
        else:
            _, _, res = recur(self.root)
            return res

    def __insert_node(self, node:Node):
        p, q = self.root, self.root
        val = node.val
        while p:
            q = p
            if p.val <= val:
                p = p.right
            else:
                p = p.left
        assert p == None and q
        if q.val <= val:
            q.right = node
        else:
            q.left = node
        node.father = q

    def insert(self, val):
        if not self.root:
            self.root = BinarySearchTree.Node(val)
        else:
            self.__insert_node(BinarySearchTree.Node(val))
        return self

    # 返回被删除的节点
    def delete(self, val):
        if not self.root:
            return None
        else:
            p = self.search(val)
            if not p:
                return p
            else:
                if not p.left and not p.right:# 没有孩子
                    fa = p.father
                    if not fa: # root
                        self.root = None
                    elif fa.left == p:
                        fa.left = None
                    else:
                        fa.right = None
                    return p
                elif p.left and p.left:# 2个孩子

                    return p
                else: # 1个孩子q, q替代p的位置
                    q = p.right
                    if p.left:
                        q = p.left
                    fa = p.father
                    if not fa:
                        self.root = q
                    elif fa.left == p:
                        fa.left = q
                    else:
                        fa.right = q
                    return p
    @staticmethod
    def make_tree(seq:List[int]):
        """
        得到的不一定是bst!.
        :param seq:
        :return:
        """
        # seq[i].left = seq[2i+1], seq[i].right = seq[2i+2]
        # for i in range(n):
        nodes = [BinarySearchTree.Node(val) if val != None
                                            else None
                                            for val in seq ]
        n = len(nodes)
        tree = BinarySearchTree()

        if n > 0:
            tree.root = nodes[0]
            for i in range(n):
                if nodes[i] == None:
                    continue
                if (i << 1) + 1 < n:
                    p = nodes[(i << 1) + 1]
                    nodes[i].left = p
                    if p:
                        p.father = nodes[i]
                else:
                    nodes[i].left = None
                if (i << 1) + 2 < n:
                    p = nodes[(i << 1) + 2]
                    nodes[i].right = p
                    if p:
                        p.father = nodes[i]
                else:
                    nodes[i].right = None
        return tree

    @staticmethod
    def find_max_node(r: Node) -> Node:
        while r and r.right:
            r = r.right
        return r

    @staticmethod
    def find_min_node(r: Node) -> Node:
        while r and r.left:
            r = r.left
        return r

    @staticmethod
    def find_min_max(r:Node) -> (Node, Node):
        return (
            BinarySearchTree.find_min_node(r),
            BinarySearchTree.find_max_node(r)
        )




    def __copy__(self):
        pass

    def __eq__(self, other):
        def equal(node1:BinarySearchTree.Node, node2:BinarySearchTree.Node) -> bool:
            if not node1 and not node2:
                return True
            elif node1 and node2:
                return node1.val == node2.val and\
                       equal(node1.left, node2.left) and\
                       equal(node1.right, node2.right)
            else:
                return False

        return equal(self.root, other.root)







