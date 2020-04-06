from typing import List


class BinaryTree:

    class Node:
        def __init__(self, key, left=None, right=None, parent=None):
            self.key = key
            self.left = left
            self.right = right
            self.parent = None

        def __repr__(self):
            return f"{self.key}"

    def __init__(self):
        self.root = None

    @staticmethod
    def make_tree(seq: List):
        nodes = [BinaryTree.Node(key) if key != None else None for key in seq]
        n = len(nodes)
        tree = BinaryTree()

        if n > 0:
            tree.root = nodes[0]
            for i in range(n):
                if nodes[i] == None:
                    continue
                if (i << 1) + 1 < n:
                    p = nodes[(i << 1) + 1]
                    nodes[i].left = p
                    if p:
                        p.parent = nodes[i]
                else:
                    nodes[i].left = None
                if (i << 1) + 2 < n:
                    p = nodes[(i << 1) + 2]
                    nodes[i].right = p
                    if p:
                        p.parent = nodes[i]
                else:
                    nodes[i].right = None
        return tree

    def preorder(self) -> list:
        st = []
        res = []
        if not self.root:
            return res
        st.append(self.root)
        while len(st) > 0:
            p = st.pop()
            res.append(p.key)
            if p.right:
                st.append(p.right)
            if p.left:
                st.append(p.left)

        # print(res)
        return res

    def preorder2(self) -> list:
        res = []
        st = []
        cur = self.root
        while cur or len(st) > 0:
            while cur:
                res.append(cur.key)
                st.append(cur)
                cur = cur.left
            p = st.pop()
            cur = p.right
        return res

    def inorder(self) -> list:
        res = []
        st = []
        cur = self.root
        while cur or len(st) > 0:
            while cur:
                # 从根节点开始
                st.append(cur)
                cur = cur.left
            # 不变量: p节点的左子树都已经push到res里了
            p = st.pop()
            res.append(p.key)
            # 若cur不为空，那么下一次将继续这个过程
            cur = p.right
        return res

    def postorder_recur(self) -> list:
        def recur(node: BinaryTree.Node):
            if node:
                recur(node.left)
                recur(node.right)
                res.append(node.key)

        res = []
        recur(self.root)
        return res

    def postorder(self) -> list:
        # 不同之处：
        # 1) 双栈，第二个栈res的翻转就是答案
        # 2)
        res = []
        st = []
        cur = self.root
        while cur or len(st) > 0:
            if cur:
                # 一直push右节点，直到遇到空节点
                st.append(cur)
                res.append(cur.key)
                cur = cur.right
            else:
                cur = st.pop().left
            # print(res)
            # print("st", st)
        res.reverse()
        return res


