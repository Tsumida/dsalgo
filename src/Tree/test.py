# 2020-01-18

from typing import List
import unittest

from src.Tree.bst import BinarySearchTree

class BSTTest(unittest.TestCase):
    def setUp(self):
        print("-"*16 + " Test -- BST " + "-"*16)

    def tearDown(self):
        print("-"*16 + "--Test done--" + "-"*16)

    def is_bst(self, tree: BinarySearchTree):
        seq = tree.inorder_seq()
        if len(seq) == 0:
            return True
        else:
            return any(seq[i] <= seq[i+1] for i in range(0, len(seq)-1))

    def test_make_tree(self):
        # normal.
        t1 = BinarySearchTree.make_tree(seq = [10, 5, 11])
        t2 = BinarySearchTree()
        r1 = BinarySearchTree.Node(10)
        r2 = BinarySearchTree.Node(5)
        r3 = BinarySearchTree.Node(11)
        r1.left = r2
        r1.right = r3
        t2.root = r1
        assert t1.root.val == t2.root.val
        assert t1 == t2

        # with None
        t1 = BinarySearchTree.make_tree(seq=[10, None, 11])
        t2 = BinarySearchTree()
        r1 = BinarySearchTree.Node(10)
        r2 = None
        r3 = BinarySearchTree.Node(11)
        r1.left = r2
        r1.right = r3
        t2.root = r1
        assert not t1.root.left and not t2.root.left
        assert t1 == t2

        # diff trees.
        t3 = BinarySearchTree.make_tree(seq=[2, 1, 3])
        assert not (t2 == t3)

        # empty tree
        assert not BinarySearchTree.make_tree(seq=[]).root

    def test_search(self):
        # didn't find
        assert not BinarySearchTree().search(1)

        # didn't find
        t0 = BinarySearchTree.make_tree(seq=[4, 2, 6, 1, 3, 5, 7])
        assert not t0.search(8)

        t1 = BinarySearchTree.make_tree(seq=[2])
        p = t1.search(2)
        assert  t1.root == p

        # found.
        t2 = BinarySearchTree.make_tree(seq=[4, 2, 6, 1, 3, 5, 7])
        p2 = t2.search(3)
        assert not p2.left and not p2.right
        p3 = t2.search(2)
        assert 1 == p3.left.val and \
               3 == p3.right.val
        assert t2.root == p3.father, f"Error: t2.root={t2.root}, p3.father={p3.father}"




    def test_find_min_max(self):
        t1 = BinarySearchTree.make_tree(seq=[10, 5, 11])
        n1, n2 = BinarySearchTree.find_min_max(t1.root)
        assert (5, 11) == (n1.val, n2.val)

        # Empty tree
        t2 = BinarySearchTree()
        n3, n4 = BinarySearchTree.find_min_max(t2.root)
        assert (None, None) == (n3, n4)

        # more
        t3 = BinarySearchTree.make_tree(seq=[4, 2, 6, 1, 3, 5, 7])
        n5, n6 = BinarySearchTree.find_min_max(t3.root)
        assert (1, 7) == (n5.val, n6.val)

        # with None.
        t3 = BinarySearchTree.make_tree(seq=[4, None, 6, None, None, 5, 7])
        n5, n6 = BinarySearchTree.find_min_max(t3.root)
        assert (4, 7) == (n5.val, n6.val)

        # with None.
        t3 = BinarySearchTree.make_tree(seq=[4, 2, None, 1, 3, None, None])
        n5, n6 = BinarySearchTree.find_min_max(t3.root)
        assert (1, 4) == (n5.val, n6.val)

    def test_is_bst(self):
        assert BinarySearchTree().is_bst()
        assert BinarySearchTree.make_tree(seq=[2, 1, 3]).is_bst()
        assert BinarySearchTree.make_tree(seq=[2, None, 3]).is_bst()
        assert BinarySearchTree.make_tree(seq=[2, 1, None]).is_bst()
        assert not BinarySearchTree.make_tree(seq=[1, 2, 3]).is_bst()
        assert BinarySearchTree.make_tree(seq=[4, 2, 6, 1, 3, 5, 7]).is_bst()
        assert BinarySearchTree.make_tree(seq=[4, 2, 6, None, 3, 5, 7]).is_bst()
        assert BinarySearchTree.make_tree(seq=[4, 2, 6, 1, None, None, 7]).is_bst()

    def test_insert(self):
        t1 = BinarySearchTree()
        t1.insert(10)
        assert t1.root.val == 10

        t2 = BinarySearchTree.make_tree(seq=[2, 1, 3])
        t2.insert(4)
        assert BinarySearchTree.make_tree(seq=[2, 1, 3, None, None, None, 4]) == t2

        t3 = BinarySearchTree.make_tree(seq=[2, 1, 3])
        t3.insert(0)
        assert BinarySearchTree.make_tree(seq=[2, 1, 3, 0]) == t3

        # 是左是右取决于插入时是 <= , >还是 <, >=
        t4 = BinarySearchTree.make_tree(seq=[2, 1, 3])
        t4.insert(1)
        assert t4.is_bst() and [1, 1, 2, 3] == t4.inorder_seq()

        # 连续插入
        t5 = BinarySearchTree.make_tree(seq=[4, 2, 6])
        t5.insert(1).insert(3).insert(5).insert(7)
        assert t5 == BinarySearchTree.make_tree(seq=[4, 2, 6, 1, 3, 5, 7])


    def test_delete(self):
        # delete nothing.
        assert not BinarySearchTree().delete(10)

        # delete root, left None.
        t1 = BinarySearchTree.make_tree(seq=[10])
        assert 10 == t1.delete(10).val
        assert not t1.root

        # delete no child
        t2 = BinarySearchTree.make_tree(seq=[2, 1, 3])
        assert 1 == t2.delete(1).val
        assert not t2.root.left and t2.is_bst(), f"t2 = {t2.inorder_seq()}"
        assert [2, 3] == t2.inorder_seq()

        # delete 1 child - left
        t3 = BinarySearchTree.make_tree(seq=[4, 2, 6, None, None, None, 7])
        assert 2 == t3.delete(2).val
        assert not t3.root.left and t3.is_bst()
        assert [4, 6, 7] == t3.inorder_seq()

        # delete 1 child - right
        t4 = BinarySearchTree.make_tree(seq=[4, 2, 6, 1, None, None, None])
        assert 6 == t4.delete(6).val
        assert not t4.root.right and t4.is_bst()
        assert [1, 2, 4] == t4.inorder_seq()

        # delete 2 child




