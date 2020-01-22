# 2020-01-20

from typing import List

class RedBlackTree:
    """
    CLRS:
    1. Each node is either red or black.
    2. The root of a rbt is black.
    3. Leaves are black.
    4. A red node must have 2 black children.
    5. For each node A, all simple paths from A to a descendant leaves, contain the same number of black nodes.

    """
    class RBTNode:
        COLOR_RED = 0
        COLOR_BLACK = 1
        def __init__(self, key, val, color,
                     left=None,
                     right=None,
                     father=None):
            self.key = key
            self.val = val
            self.color = color
            self.right = right
            self.left = left
            self.father = father

        def __repr__(self):
            return "(key={}, val={}, left={}, right={}, father={})".format(
                self.key, self.val, id(self.left), id(self.right), id(self.father)
            )

        def __eq__(self, other):
            if self and other:
                return id(self) == id(other) # 防止无限递归
            elif not self and not other:
                return True
            else:
                return False

        def set_black(self):
            self.color = RedBlackTree.RBTNode.COLOR_BLACK

        def set_red(self):
            self.color = RedBlackTree.RBTNode.COLOR_RED

        def get_kv(self):
            return self.key, self.val

    def __init__(self):
        self.__init_leaf()
        self.__root = self.__nil

    def __eq__(self, other):
        pass

    def __init_leaf(self):
        self.__nil = RedBlackTree.RBTNode(None, None, color=RedBlackTree.RBTNode.COLOR_BLACK)
        self.__nil.left = self.__nil
        self.__nil.right = self.__nil
        self.__nil.father = self.__nil

    '''
    #===============================================================
              y                                           x
             / \       <-------- left  rotate -------    / \
            x   c                                       a   y
           / \         --------- right rotate ------>      / \
          a   b                                           a   b
    #===============================================================
    恢复原状:
    left_rotate(x).right_rotate(x.father) 或者
    right_rotate(y).left_rotate(y.father)
    '''

    def __left_rotate(self, x:RBTNode):
        y = x.right
        x.right = y.left
        if y.left != self.__nil:
            y.left.father = x
        y.father = x.father
        if x.father == self.__nil:
            self.__root = y
        elif x == x.father.left:
            x.father.left = y
        else:
            x.father.right = y
        y.left = x
        x.father = y

        return self

    def __right_rotate(self, y: RBTNode):
        # right rotate is symmetric.
        x = y.left
        y.left = x.right
        if x.right != self.__nil:
            x.right.father = y
        x.father = y.father
        if y.father == self.__nil:
            self.__root = x
        elif y == y.father.left:
            y.father.left = x
        else:
            y.father.right = x
        x.right = y
        y.father = x
        return self

    def __insert_node(self, node: RBTNode):
        leaf = self.__nil
        y = self.__nil
        x = self.__root
        while x != leaf:
            y = x
            if node.key <= x.key:
                x = x.left
            else:
                x = x.right
        node.father = y
        if y == leaf:
            self.__root = node
        elif node.key <= y.key:
            y.left = node
        else:
            y.right = node
        # 以上都是常见的BST插入
        self.__insert_fixup(node)
        return self

    def __delete_node(self, node:RBTNode):
        """
        CLRS: page 324

        :param node:
        :return:
        """
        assert node
        z, y = node, node
        x = None
        y_origin_color = y.color
        if z.left == self.__nil:
            x = z.right
            self.__transplant(z, z.right)
        elif z.right == self.__nil:
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = self.__find_min(z.right)
            y_origin_color = y.color
            x = y.right
            if y.father == z:
                x.father = y
            else:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.father = y
            self.__transplant(z, y)
            y.left = z.left
            y.left.father = y
            y.color = z.color
        if y_origin_color == RedBlackTree.RBTNode.COLOR_BLACK:
            self.__delete_fixup(x)

    def __find_min(self, node:RBTNode) -> RBTNode:
        leaf = self.__nil
        assert node != leaf
        while node != leaf and node.left != leaf:
            node = node.left
        return node

    def __find_max(self, node:RBTNode) -> RBTNode:
        leaf = self.__nil
        assert node != leaf
        while node != leaf and node.right != leaf:
            node = node.right
        return node

    def __transplant(self, u:RBTNode, v:RBTNode):
        if u.father == self.__nil:
            self.__root = v
        elif u == u.father.left:
            u.father.left = v
        else:
            u.father.right = v
        v.father = u.father

    def __search_node(self, key):
        p = self.__root
        while p != self.__nil:
            if p.key == key:
                break
            elif p.key < key:
                p = p.right
            else:
                p = p.left
        return p

    def __insert_fixup(self, node:RBTNode):
        """
        Insertion only violates property 2 & 4.
        1. The root must be black.
        2. A red node must have 2 black children.

        :param node:
        :return:
        """
        z = node
        red = RedBlackTree.RBTNode.COLOR_RED
        black = RedBlackTree.RBTNode.COLOR_BLACK
        while z.father.color == red: # 表明z.father.father存在

            if z.father == z.father.father.left:
                y = z.father.father.right # z's sibling
                if y.color == red: # ---------------------------------------- case 1, y是红色
                    z.father.color = black
                    y.color = black
                    z.father.father.color = red
                    z = z.father.father
                else:
                    if z == z.father.right: # ------------------------------------ case 2
                        z = z.father
                        self.__left_rotate(z)
                    # ------------------------------------------------------- case 3
                    z.father.color = black
                    z.father.father.color = red
                    self.__right_rotate(z.father.father)
            else: # 上面三种和下面三种是对称的
                y = z.father.father.left # z's sibling
                if y.color == red: # ---------------------------------------- case 4
                    z.father.color = black
                    y.color = black
                    z.father.father.color = red
                    z = z.father.father
                else:
                    if z == z.father.left: # ------------------------------------- case 5
                        z = z.father
                        self.__right_rotate(z)
                    # ------------------------------------------------------- case 6
                    z.father.color = black
                    z.father.father.color = red
                    self.__left_rotate(z.father.father)
        self.__root.color = black

    def __delete_fixup(self, node:RBTNode):
        """

        :param node:
        :return:
        """
        x = node
        leaf, root = self.__nil, self.__root
        red, black = RedBlackTree.RBTNode.COLOR_RED, RedBlackTree.RBTNode.COLOR_BLACK
        while x != root and x.color == black:
            if x == x.father.left:
                w = x.father.right
                if w.color == red: # --------------------------------------------- case 1
                    w.color = black
                    x.father.color = red
                    self.__left_rotate(x.father)
                    w = x.father.right
                if w.left.color == black and w.right.color == black: # ----------- case 2
                    w.color = red
                    x = x.father
                else:
                    if w.right.color == black: # --------------------------------- case 3
                        w.left.color = black
                        w.color = red
                        self.__right_rotate(w)
                        w = x.father.right
                    w.color = x.father.color # ----------------------------------- case 4
                    x.father.color = black
                    w.right.color = black
                    self.__left_rotate(x.father)
                    x = self.__root
            else:
                w = x.father.left
                if w.color == red:
                    w.color = black
                    x.father.color = red
                    self.__right_rotate(x.father)
                    w = x.father.left
                if w.left.color == black and w.right.color == black:
                    w.color = red
                    x = x.father
                else:
                    if w.left.color == black:
                        w.right.color = black
                        w.color = red
                        self.__left_rotate(w)
                        w = x.father.left
                    w.color = x.father.color
                    x.father.color = black
                    w.left.color = black
                    self.__right_rotate(x.father)
                    x = self.__root
        x.color = black

    @staticmethod
    def make_tree(key_seq:List, val_seq:List, color_seq:List):
        n = len(key_seq)
        assert n >= 0 and\
               n == len(val_seq) and\
               n == len(color_seq)
        #if n == 0:
        #    print("Empty seq.")
        tree = RedBlackTree()
        leaf = tree.__nil

        nodes = [
            RedBlackTree.RBTNode(key_seq[i], val_seq[i], color_seq[i])
            if key_seq[i] else leaf # key_seq[i] == None --> link with leaf.
            for i in range(n)
        ]
        if n > 0:
            root = tree.set_root(nodes[0])
            root.father = leaf
            for i in range(n):
                if nodes[i] == leaf:
                    continue
                if (i << 1) + 1 < n:
                    p = nodes[(i << 1) + 1]
                    nodes[i].left = p
                    if p != leaf:
                        p.father = nodes[i]
                else:
                    nodes[i].left = leaf
                if (i << 1) + 2 < n:
                    p = nodes[(i << 1) + 2]
                    nodes[i].right = p
                    if p != leaf:
                        p.father = nodes[i]
                else:
                    nodes[i].right = leaf
        return tree

    def set_root(self, new_root:RBTNode):
        assert new_root
        self.__root = new_root
        return self.__root

    def get_level(self, node:RBTNode) -> int:
        if node != self.__nil:
            l, r = 0, 0
            if node.left != self.__nil:
                l = self.get_level(node.left)
            if node.right != self.__nil:
                r = self.get_level(node.right)
            return 1 + max(l, r)
        else:
            return 0

    def get_root(self) -> RBTNode:
        return self.__root

    def get_leaf(self) -> RBTNode:
        return self.__nil

    def get_inorder_seq(self):
        # 把左子节点链存到st
        # 那么st[-1]一定是某颗子树中最小的节点, left为叶子
        # 关键在于把 L v R --> L v R v R --> ... --> v R v R ... v R
        leaf = self.__nil
        if self.__root == leaf:
            return []
        st = []
        res = []
        cur = self.__root
        while cur != leaf or len(st) > 0: # 因为这里st只保存了左链的节点,
            while cur != leaf:
                st.append(cur)
                cur = cur.left
            p = st.pop()
            res.append((p.key, p.val))
            cur = p.right
        return res

    def is_leaf(self, node: RBTNode) -> bool:
        return self.__nil == node

    def is_rbt(self) -> (bool, str):
        def property_4(node:RedBlackTree.RBTNode):
            if node != leaf:
                if node.color == red and\
                        (node.left.color == red or node.right.color == red):
                    raise RBTException(node,
                                       "red node has at least one red child.")
                else:
                    # may raise error
                    property_4(node.left)
                    property_4(node.right)

        def property_5(node:RedBlackTree.RBTNode):
            if node == leaf:
                return 1
            else:
                l = property_5(node.left)
                r = property_5(node.right)
                if l != r:
                    raise RBTException(node, f"different black height left={l}, right={r}")
                if node.color == red:
                    return l
                else :
                    return l + 1

        root, leaf = self.__root, self.__nil
        red, black = RedBlackTree.RBTNode.COLOR_RED, RedBlackTree.RBTNode.COLOR_BLACK
        if root.color == red:
            return False, "error: root is red."
        if leaf.color == red:
            return False, "error: leaf is red."
        try:
            # assert that root is black and leaf is black.
            property_4(self.__root)
            _ = property_5(self.__root)
        except RBTException as e:
            return False, str(e)

        return True, ""



    # Return (key, val) for the first node with node.key == key.
    # Else return (key, None)
    def search(self, key):
        p = self.__search_node(key)
        if p == self.__nil:
            return key, None
        else:
            return p.key, p.val

    def insert(self, key, val):
        leaf = self.__nil
        node = RedBlackTree.RBTNode(key, val, RedBlackTree.RBTNode.COLOR_RED, leaf, leaf, leaf)
        return self.__insert_node(node)

    def delete(self, key):
        p = self.__search_node(key)
        if p == self.__nil:
            return key, None
        else:
            self.__delete_node(p)
            return p.key, p.val

    def inorder_seq(self) -> List:
        def recur(node:RedBlackTree.RBTNode, lis:List):
            if node:
                recur(node.left, lis)
                lis.append((node.key, node.val))
                recur(node.right, lis)

        res = []
        recur(self.__root, res)
        return res

class RBTException(Exception):
    def __init__(self, node:RedBlackTree.RBTNode, msg:str):
        self.node = node
        self.msg = msg

    def __str__(self):
        return "RBTException: node({})\nmsg={}".format(self.node, self.msg)

