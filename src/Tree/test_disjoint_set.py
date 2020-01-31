# 2020-01-29

from unittest import TestCase
from random import randint, choice
from src.Tree.disjoint_set import DisjointSet
from cProfile import Profile

class TestDisjointSet(TestCase):

    __CASES = {
        # "empty"
        #
        "c1": [1, 2, 3, 4, 5, 6, 7],
        "c2": [2],
        "c3": [],
    }

    def test_make_set(self):
        c1 = [1, 2, 3, 4, 5, 6, 7]
        ds1 = DisjointSet(c1)
        assert all(ds1.find_repr(x) == x for x in c1)

        c2 = [2]
        ds2 = DisjointSet(c2)
        assert not ds2.is_empty()
        assert ds2.find_repr(2) == 2

        c3 = []
        assert DisjointSet(c3).is_empty()

    def test_find_repr(self):
        c1 = [1, 2, 3, 4, 5, 6, 7]
        ds1 = DisjointSet(c1)
        # [1, 2, 3, 4], [5], [6], [7]
        ds1.union(1, 2)\
            .union(1, 3)\
            .union(1, 4)
        assert ds1.find_repr(2) == 1, f"error: {ds1.get_sets()}"
        assert ds1.find_repr(3) == 1
        assert ds1.find_repr(4) == 1

        ds1.union(5, 1)
        assert ds1.find_repr(1) == 5

    def test_union(self):
        c1 = [1, 2, 3, 4, 5, 6, 7]
        ds1 = DisjointSet(c1)
        ds1.union(1, 2).union(1, 3)

        assert ds1.find_repr(2) == 1
        assert ds1.find_repr(3) == 1

        ds1.union(3, 5)
        assert ds1.find_repr(5) == 1

        ds2 = DisjointSet(c1)
        ds2.union(1, 2).union(2, 3).union(3, 4)
        # [[1, 2, 3, 4], [5, 6, 7]]
        assert ds2.find_repr(3) == 1
        assert ds2.find_repr(4) == 1
        ds2.union(5, 6).union(6, 7)
        assert ds2.find_repr(6) == 5
        assert ds2.find_repr(7) == 5

        # ====================================
        #    1       5                1
        #  2 3 4   6   7  ---->  2 3 4 5 6 7
        # ====================================
        ds2.union(3, 6)
        assert ds2.find_repr(5) == 1
        assert ds2.find_repr(6) == 1
        assert ds2.find_repr(7) == 1

    def test_is_equivalent(self):
        c1 = self.__CASES["c1"]
        ds1 = DisjointSet(c1)
        assert ds1.is_equivalent(1, 1)
        assert not ds1.is_equivalent(1, 2)
        ds1.union(1, 2)
        assert ds1.is_equivalent(1, 2)
        ds1.union(1, 3)
        assert ds1.is_equivalent(1, 3)

    def test_get_resps(self):
        c1 = self.__CASES["c1"]
        ds1 = DisjointSet(c1)
        assert c1 == ds1.get_resps()

        ds1.union(1, 2).union(1, 3).union(1, 4)
        assert [1, 5, 6, 7] == ds1.get_resps()

        ds1.union(5, 1).union(5, 6)
        assert [5, 7] == ds1.get_resps()
        ds1.union(7, 5)
        assert [7] == ds1.get_resps()
        ds1.union(7, 7)
        assert [7] == ds1.get_resps()

    def test_get_sets(self):
        c1 = self.__CASES["c1"]
        ds1 = DisjointSet(c1)
        r1 = ds1.get_sets()
        assert [
            [1], [2], [3], [4], [5], [6], [7]
        ] == sorted(r1), f"Error, got :{r1}"

        ds1.union(1, 2).union(1, 3).union(1, 4)
        r2 = ds1.get_sets()
        assert len(r2) == 4, f"Error, got: {r2}"
        assert [1, 5, 6, 7] == [line[0] for line in r2]
        assert len(r2[0]) == 4 # [1, 2, 3, 4]为一个集合

        assert [[2]] == DisjointSet(self.__CASES["c2"]).get_sets()
        assert [] == DisjointSet(self.__CASES["c3"]).get_sets()

    def test_perf(self):
        def test_union(ds: DisjointSet, random_seq):
            for a, b in random_seq:
                ds.union(a, b)

        n = 64000
        random_key = list(set(randint(0, n) for _ in range(n)))
        n = len(random_key)
        random_tup = [(choice(random_key), choice(random_key)) for _ in range(n << 1)]
        ds = DisjointSet(random_key)
        print("-"*32)

        p2 = Profile()
        p2.runcall(test_union, ds=ds, random_seq=random_tup)
        p2.print_stats()
        print("-"*32, "n = ", n)

        levels = ds.get_levels()
        for c, num in levels:
            print("level = {}, num = {:8}, per = {}".format(c, num, round(num / n, 4)))

        print("Expected level: ", round(sum(c * num / n for c, num in levels), 4))



