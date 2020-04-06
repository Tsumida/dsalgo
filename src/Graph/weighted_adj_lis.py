
from typing import List, Tuple
from src.Graph.graph_storage import *
from src.Graph.others import *

class WeightedAdjLis(GraphStorage):
    """
    带权的邻接表，不含多重边
    (u, v, w)表示 从u到v的带权有向边
    """
    class __Edge:
        def __init__(self, v, w):
            self.v = v
            self.w = w

    def __init__(self):
        super(WeightedAdjLis, self).__init__()
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
        nodes = self.__adj.setdefault(u, list())
        if any(v == nod.v for nod in nodes):
            raise GraphException(ERR_EDGE_EXISTS.format((u, v)))

        nodes.append(WeightedAdjLis.__Edge(v, w))
        if v not in self.__adj:
            self.add_node(v)
        return self

    def del_edge(self, u, v):
        # 删除边并返回
        # O(E)
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
        if node in self.__adj:
            raise GraphException(ERR_NODE_EXISTS.format(node))
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
            s = f"key={k}, "
            vs = ", ".join(f"({v}, {w})" for v, w in sorted(lis))
            print(s+vs)

    def storage_type(self):
        return PHY_ADJ_LIS

    def nodes(self):
        # O(V)
        return [x for x in self.__adj.keys()]

    def edges(self):
        # O(V+E)
        res = []
        res.extend(
            [(u, nod.v, nod.w) for u, lis in self.__adj.items()
                                for nod in lis ]
        )
        return res

    @staticmethod
    def make(edges:List[Tuple]):
        """
        edges = List[Tuple(u, v, w)], where u and v is hashable and w is numeric.
        :param edgs:
        :return:
        """
        g = WeightedAdjLis()
        for u, v, w in edges:
            g.add_edge(u, v, w)
        return g

    def transposition(self):
        t = WeightedAdjLis()
        for u, s in self.__adj.items():
            # (u, v, w) -> (v, u, w)
            for edge in s:
                t.add_edge(edge.v, u, edge.w)
        return t

    def __eq__(self, other):
        for u, s in other.__adj.items():
            for oedge in s:
                try:
                    res = self.get_edge(u, oedge.v)
                    if res == None: return False
                    _, _, sw = res
                    if sw != oedge.w: return False
                except GraphException: return False
        return True









