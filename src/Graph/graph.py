# 2020-02-03

from abc import ABC
from typing import List, Tuple

class Graph:

    __PHY_MAT = "matrix"
    __PHY_ADJ_LIS = "adjacent lis"

    def __init__(self, phy=__PHY_ADJ_LIS):
        pass


class WeightedAdjLis:
    """
    带权的邻接表，不含多重边
    (u, v, w)表示 从u到v的带权有向边
    """
    class __Edge:
        def __init__(self, v, w):
            self.v = v
            self.w = w

    def __init__(self):
        self.__adj = dict()

    def get_num_node(self):
        # O(1)
        return len(self.__adj)

    def get_num_edge(self):
        # O(V)
        return sum(len(v) for v in self.__adj.values())

    def get_edge(self, u, v):
        # 返回 (u, v, w) 或者 None
        p = self.__adj.get(u, None)
        if p:
            for node in p:
                if v == node.v:
                    return (u, v, node.w)
        return None

    def add_edge(self, u, v, w):
        # O(E)
        # if u or v not in self.__adj, add new node.
        node = self.__adj.setdefault(u, list())
        assert all(v != nod.v for nod in node), f"Error: edge({u}, {v}) exists."
        node.append(WeightedAdjLis.__Edge(v, w))
        if v not in self.__adj:
            self.add_node(v)
        return self

    def del_edge(self, u, v):
        # 删除边并返回
        q = self.__adj.get(u, None)
        res = None
        index = -1
        if q:
            for i, node in enumerate(q):
                if node.v == v:
                    index = i
                    res = (u, v, node.w)
            if index != -1:
                q.pop(index)
        return res

    def contains_edge(self, u, v):
        # O(E)
        # 时候有一条从u到v的有向边
        p = self.__adj.get(u, None)
        if not p:
            return False
        else:
            return any(node.v == v for node in p)

    def get_neighbours(self, node):
        # O(E)
        # 获得点所有的出边
        return [(nod.v, nod.w) for nod in self.__adj.get(node, list())]

    def add_node(self, node):
        assert node not in self.__adj, f"Error: node{node} exists."
        self.__adj[node] = list()
        return self

    def del_node(self, node):
        # O(V + E)
        # 删除所有与node关联的边
        if node in self.__adj:
            del self.__adj[node]
        for k, lis in self.__adj.items():
            index = -1
            for i, nod in enumerate(lis):
                if nod.v == node:
                    index = i
                    break # 最多只含一条边
            if index != -1:
                lis.pop(index)

    def set_weight(self, u, v, new_weight):
        lis = self.__adj.get(u, None)
        if lis:
            for nod in lis:
                if nod.v == v:
                    nod.w = new_weight
                    break
        return self


    def contains_node(self, node):
        return node in self.__adj

    def print_status(self):
        kvs = [(k, self.get_neighbours(k)) for k in sorted(self.__adj.keys())]
        kvs.sort(key=lambda p:p[0])

        for k, lis in kvs:
            s = f"key={k}\t"
            vs = ", ".join(f"({v}, {w})" for v, w in sorted(lis))
            print(s+vs)


    @staticmethod
    def from_edge_list(edges:List[Tuple]):
        """
        edges = List[Tuple(u, v, w)], where u and v is hashable and w is numeric.
        :param edgs:
        :return:
        """
        g = WeightedAdjLis()
        for u, v, w in edges:
            g.add_edge(u, v, w)
        return g

