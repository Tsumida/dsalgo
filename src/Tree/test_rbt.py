# 2020-01-20
import unittest
from random import randint

from src.Tree.rbt import RedBlackTree

class TestRBT(unittest.TestCase):

    def get_color(self) -> (int, int):
        return (RedBlackTree.RBTNode.COLOR_RED,
                RedBlackTree.RBTNode.COLOR_BLACK)

    def test_make_tree(self):
        red, black = self.get_color()
        t1 = RedBlackTree()
        assert  t1.is_leaf(t1.get_root())

        case_1 = {
            'key_seq' : [2, 1, 3],
            'val_seq' : ["666", "233", "888"],
            'color_seq' : [black, red, red],
        }
        t2 = RedBlackTree.make_tree(**case_1)
        root = t2.get_root()
        assert root.color == black and root.key == 2 and root.val == "666", f"error: \n{root}"
        assert root.left.key == 1 and root.right.key == 3

        case_2 = {
            'key_seq' : [4, 2, 6, 1, 3, 5, 7],
            'val_seq' : ["abc", "def", "hji", "klm", "nop", "rst", "uvw"],
            'color_seq' : [black, red, red, black, black, black, black],
        }
        _ = RedBlackTree.make_tree(**case_2)


        case_3 = {
            'key_seq' : [4, 2, 6, None, 3, 5, None], # None -> link leaf not None
            'val_seq' : ["abc", "def", "hji", "klm", "nop", "rst", "uvw"],
            'color_seq' : [black, red, red, black, black, black, black],
        }
        t4 = RedBlackTree.make_tree(**case_3)
        root = t4.get_root()
        assert root.left.left == t4.get_leaf()
        assert root.right.right == t4.get_leaf()

    def test_search(self):
        red, black = self.get_color()
        # found
        case_1 = {
            'key_seq' : [2, 1, 3],
            'val_seq' : ["666", "233", "888"],
            'color_seq' : [black, red, red],
        }
        t1 = RedBlackTree.make_tree(**case_1)
        assert (2, "666") == t1.search(2)
        assert (1, "233") == t1.search(1)
        assert (3, "888") == t1.search(3)

        # not found
        assert (5, None) == t1.search(5)



    def test_insert(self):
        red, black = self.get_color()

        # new root
        t1 = RedBlackTree()
        t1.insert(5, "666")
        assert (5, "666") == t1.get_root().get_kv()

        # normal insert
        case_1 = {
            'key_seq' : [2, 1, 3],
            'val_seq' : ["666", "233", "888"],
            'color_seq' : [black, red, red],
        }

        t2 = RedBlackTree.make_tree(**case_1)
        t2.insert(5, "777").insert(0, "333")
        r2 = t2.get_root()
        assert (5, "777") == r2.right.right.get_kv()
        assert (0, "333") == r2.left.left.get_kv()
        assert r2.color == black
        assert r2.left.color == black and r2.right.color == black

        # continuous insertions.
        t3 = RedBlackTree()
        a, b, n = 0, 10000, 1000
        random_key = [randint(a, b) for _ in range(n)]
        for key in random_key:
            t3.insert(key, randint(0, 9))
        #print("level = ", t3.get_level(t3.get_root()))

    def test_delete(self):
        red, black = self.get_color()

        # empty
        t1 = RedBlackTree()
        assert (1, None) == t1.delete(1)

        t2 = RedBlackTree().insert(2, "666")
        assert (2, "666") == t2.delete(2)
        assert t2.is_leaf(t2.get_root())

        case_3 = {
            'key_seq' : [2, 1, 3],
            'val_seq' : ["666", "233", "888"],
            'color_seq' : [black, red, red],
        }
        t3 = RedBlackTree.make_tree(**case_3)
        assert (3, "888") == t3.delete(3)
        assert (1, "233") == t3.delete(1)
        assert (2, "666") == t3.delete(2)
        assert t2.is_leaf(t2.get_root())

    def test_inorder_seq(self):
        red, black = self.get_color()

        assert [] == RedBlackTree().get_inorder_seq()

        case_2 = {
            'key_seq' : [2, 1, 3],
            'val_seq' : ["666", "233", "888"],
            'color_seq' : [black, red, red],
        }
        t2 = RedBlackTree.make_tree(**case_2)
        seq = t2.get_inorder_seq()
        assert [(1, "233"), (2, "666"), (3, "888")] == seq, f"\n{seq}"

        t3 = RedBlackTree()
        a, b, n = 0, 30000, 10000
        random_key = [randint(a, b) for _ in range(n)]
        for key in random_key:
            t3.insert(key, randint(0, 9))

        key_seq = [key for key, _ in t3.get_inorder_seq()]

        assert [key_seq[i] <= key_seq[i+1] for i in range(n-1)]




















