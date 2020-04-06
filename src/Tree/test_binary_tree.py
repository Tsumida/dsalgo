from unittest import TestCase

from src.Tree.binary_tree import BinaryTree

class TestDisjointSet(TestCase):

    __CASE = {
        '7-complete': [1, 2, 3, 4, 5, 6, 7],
        '4-left-link-list': [1, 2, None, 4, None, None, None, 5],
        'single': [1],
        'empty' : [],
        '5-non-complete': [1, 2, 3, None, None, 4, 5],
    }

    def test_preorder2(self):
        t = BinaryTree.make_tree(self.__CASE['7-complete'])
        res = t.preorder2()
        assert [1, 2, 4, 5, 3, 6, 7] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['4-left-link-list'])
        res = t.preorder2()
        assert [1, 2, 4, 5] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['single'])
        res = t.preorder2()
        assert [1] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['empty'])
        res = t.preorder2()
        assert [] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['5-non-complete'])
        res = t.preorder2()
        assert [1, 2, 3, 4, 5] == res, f"right={res}"

    def test_preorder(self):
        t = BinaryTree.make_tree(self.__CASE['7-complete'])
        res = t.preorder()
        assert [1, 2, 4, 5, 3, 6, 7] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['4-left-link-list'])
        res = t.preorder()
        assert [1, 2, 4, 5] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['single'])
        res = t.preorder()
        assert [1] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['empty'])
        res = t.preorder()
        assert [] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['5-non-complete'])
        res = t.preorder()
        assert [1, 2, 3, 4, 5] == res

    def test_inorder(self):
        t = BinaryTree.make_tree(self.__CASE['7-complete'])
        res = t.inorder()
        assert [4, 2, 5, 1, 6, 3, 7] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['4-left-link-list'])
        res = t.inorder()
        assert [5, 4, 2, 1] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['single'])
        res = t.inorder()
        assert [1] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['empty'])
        res = t.inorder()
        assert [] == res, f"right={res}"

        t = BinaryTree.make_tree(self.__CASE['5-non-complete'])
        res = t.inorder()
        assert [2, 1, 4, 3, 5] == res, f"right={res}"

    def test_postorder(self):
        for label, case in self.__CASE.items():
            t = BinaryTree.make_tree(case)
            recur = t.postorder_recur()
            iter = t.postorder()
            assert recur == iter, f"label={label}\nrecur:\n{recur}\niter:\n{iter}"
            break
