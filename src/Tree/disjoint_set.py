# 2020-01-29

import types
from typing import List, Set, Iterable

class DisjointSet:

    def __init__(self, collect:iter):
        collect = set(collect)
        self.__inner = dict()
        for ele in collect:
            self.__inner[ele] = ele

    def find_repr(self, x):
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

    def union(self, x, y):
        s_x = self.find_repr(x)
        s_y = self.__inner[y]
        if s_y != s_x:
            tmp = y
            p = s_y
            # 同一个集合所有元素都是等价的
            # 下面的循环将更新在y之上的所有节点
            # 树中其他分支的更新将延迟到调用 find_repr(), union()
            while tmp != p: # [[1], [2]], union(1, 2), 不进入循环
                self.__inner[tmp] = s_x
                tmp = p
                p = self.__inner[tmp]
            self.__inner[p] = s_x # p此时为原y集合的代表元
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
        return self.find_repr(x) == self.find_repr(y)

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

    def get_levels(self):
        vals = [val for val in self.__inner.values()]
        levels = dict()
        for i, x in enumerate(vals):
            cnt = 1
            p = self.__inner[x]
            prev = x
            while p != prev:
                prev = p
                p = self.__inner[prev]
                cnt += 1
            if cnt not in levels:
                levels[cnt] = 1
            else:
                levels[cnt] += 1
        res = [(c, n) for c, n in levels.items()]
        res.sort(key=lambda t: t[0])
        return res




