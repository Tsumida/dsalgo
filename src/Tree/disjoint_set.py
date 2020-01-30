# 2020-01-29

import types
from typing import List, Set, Iterable

class DisjointSet:

    def __init__(self, collect:iter):
        collect = set(collect)
        self.__inner = dict()
        for ele in collect:
            self.__inner[ele] = ele

    def find_resp(self, x):
        # O(log log n)
        p = self.__inner[x]
        prev = x
        while p != prev:
            tmp = prev
            prev = p
            p = self.__inner[prev]
            self.__inner[tmp] = p
        self.__inner[x] = p
        return p

    def make_set(self, x):
        assert x not in self.__inner
        self.__inner[x] = x
        return self

    # 将y子树简单合并到x所在的集合
    def union(self, x, y):
        # case 1: x == y
        # case 2: x.p.p ... = y
        # case 3: y.p.p ... = x
        s_x = self.find_resp(x)
        s_y = self.find_resp(y)
        if s_x != s_y:
            self.__inner[y] = s_x

        return self

    def is_empty(self):
        return len(self.__inner) == 0

    def get_resps(self):
        return [
            k for k, v in self.__inner.items() if k == v
        ]

    def get_sets(self):
        tmp = dict()
        resps = self.get_resps()
        for ele in resps:
            tmp[ele] = [ele]
        for v, resp in self.__inner.items():
            if v != resp:
                tmp[resp].append(v)

        res = [line for line in tmp.values()]
        res.sort(key=lambda line: line[0])
        return res

    def is_equivalent(self, x, y):
        return self.find_resp(x) == self.find_resp(y)

    def contains(self, x):
        return x in self.__inner

    @staticmethod
    def from_list(set_seq: List[List]):
        resps = [c[0] for c in set_seq]
        res = DisjointSet(resps)

        for c in set_seq:
            resp = c[0]
            for ele in c[1:]:
                res.make_set(ele)
                res.union(resp, ele)

        return res

    def max_level(self) -> int:
        vals = [val for val in self.__inner.values()]
        levels = [0 for _ in range(len(vals))]
        for i, x in enumerate(vals):
            cnt = 1
            p = self.__inner[x]
            prev = x
            while p != prev:
                prev = p
                p = self.__inner[prev]
                cnt += 1
            levels[i] = cnt

        return max(levels)




