# 2020-02-03

from abc import ABC
from typing import List, Tuple
# =================================================================================
# err msg
ERR_INVALID_STORAGE_TYPE = "Error, invalid storage type: {}"
ERR_NODE_EXISTS = "Error, node {} exists."
ERR_EDGE_EXISTS = "Error, edge {} exists."
# =================================================================================

PHY_MAT = "matrix"
PHY_ADJ_LIS = "adjacent lis"
# =================================================================================


class GraphException(Exception):
    def __init__(self, msg:str):
        self.msg = msg

    def __str__(self):
        return self.msg

class Graph:


    def __init__(self):
        self.__storage = None
        self.__type = None

    def set_type(self, type):
        if type == PHY_ADJ_LIS or type == PHY_MAT:
            self.__type = type
        else:
            raise GraphException(ERR_INVALID_STORAGE_TYPE.format(type))
        return self

    def get_type(self) -> str:
        return self.__type

    def get_storage(self):
        return self.__storage

    def from_list(self, lis:List[Tuple]):
        if self.__type == PHY_ADJ_LIS:
            self.__storage = WeightedAdjLis.from_edge_list(lis)
        elif self.__type == PHY_MAT:
            self.__storage = AdjMat.from_edge_list(lis)
        else:
            raise GraphException(ERR_INVALID_STORAGE_TYPE.format(self.__type))
        return self

    @staticmethod
    def from_edge_list(type, edges:List[Tuple]):
        return Graph().set_type(type).from_list(edges)

class GraphStorage(ABC):

    def __init__(self):
        pass
    def get_num_node(self):
        pass

    def get_num_edge(self):
        pass

    def get_edge(self, u, v):
        # 返回 (u, v, w) 或者 None
        pass

    def add_edge(self, u, v, w):
        # if u or v not in G.V, add new node.
        pass

    def del_edge(self, u, v):
        # 删除边并返回
        pass

    def contains_edge(self, u, v):
        # 判断是否包含一条边(u, v)
        pass

    def get_neighbours(self, node):
        # 获得点所有的出边
        pass

    def add_node(self, node):
        pass

    def del_node(self, node):
        # 删除所有与node关联的边
        pass

    def set_weight(self, u, v, new_weight):
        pass

    def contains_node(self, node):
        pass

    def print_status(self):
        pass

    def storage_type(self):
        pass

    @staticmethod
    def from_edge_list(edges:List[Tuple]):
        pass

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

class AdjMat(GraphStorage):

    def __init__(self):
        super(AdjMat, self).__init__()
        self.__mat = list()
        self.__node2index = dict()
        self.__index2node = dict()

    def __edge2index(self, u, v):
        return (self.__node2index.get(u, None),
                self.__node2index.get(v, None))

    def __assert_regular(self):
        assert len(self.__node2index) == len(self.__mat),\
            f"Error: node2index={self.__node2index}, mat={self.__mat}"

    def __regularize(self):
        """
        负责删除节点后的整理工作， 保证self.__cnt
                      del
                      |
                  0 1 2 3            0 1 2
                0 1 2 7 3          0 1 2 3
                1 2 3 9 N   ---->  1 2 3 N
        del --- 2 None             2 3 N N
                3 3 N 5 N

        """

        to_del = dict()  # 被删除的节点的下标
        for n, i in self.__node2index.items():
            if self.__mat[i] == None:
                to_del[i] = n

        rehash_map = dict() # label -> index
        new_mat = []
        for i, line in enumerate(self.__mat):
            if line:
                new_mat.append([x for i, x in enumerate(line) if i not in to_del])
                rehash_map[self.__index2node[i]] = len(new_mat) - 1

        self.__node2index = rehash_map
        self.__index2node = dict()
        for k, v in self.__node2index.items():
            self.__index2node[v] = k
        self.__mat = new_mat


    def get_num_node(self):
        return len(self.__node2index)

    def get_num_edge(self):
        # O(V^2)
        cnt = 0
        for line in self.__mat:
            cnt += sum(1 for x in line if x )
        return cnt

    def get_edge(self, u, v):
        # 返回 (u, v, w) 或者 None
        a, b = self.__edge2index(u, v)
        if a != None and b != None:
            return (u, v, self.__mat[a][b])
        else:
            return None

    def add_edge(self, u, v, w):
        # if u or v not in G.V, add new node.
        # if (u, v) exists, raise GraphException
        if u not in self.__node2index:
            self.add_node(u)
        if v not in self.__node2index:
            self.add_node(v)

        a, b = self.__node2index[u], self.__node2index[v]
        if self.__mat[a][b]:
            raise GraphException(ERR_EDGE_EXISTS.format((u, v)))
        self.__mat[a][b] = w
        return self

    def del_edge(self, u, v):
        # 删除边并返回
        a, b = self.__edge2index(u, v)
        if a != None and b != None:
            val = self.__mat[a][b]
            if val:
                self.__mat[a][b] = None
                return u, v, val
        return None

    def contains_edge(self, u, v):
        # 判断是否包含一条边(u, v)
        a, b = self.__edge2index(u, v)

        return a != None and b != None and self.__mat[a][b]

    def get_neighbours(self, node):
        # 获得点所有的出边
        # usage: for v, w in graph.get_neighbours("z city")
        a = self.__node2index.get(node, None)
        if a != None:
            return [(self.__index2node[i], v) for i, v in enumerate(self.__mat[a]) if v != None]
        else:
            return list()

    def add_node(self, node):
        if node in self.__node2index:
            raise GraphException(ERR_NODE_EXISTS.format(node))

        # 前置条件: 矩阵是紧密的
        self.__assert_regular()
        n = len(self.__mat)
        if n == 0:
            self.__mat.append([None])
        else:
            # 每一行都增加一列
            for line in self.__mat:
                line.append(None)
            # 增加一行
            self.__mat.append([None] * (n+1))

        self.__node2index[node] = n
        self.__index2node[n] = node
        # 后置条件: 矩阵是紧密的
        self.__assert_regular()


    def del_node(self, node):
        # O(--========================================
        # 删除所有与node关联的边
        self.__assert_regular()
        index = self.__node2index.get(node, None)
        if index != None:
            self.__mat[index] = None # 标记node的行为None
            self.__regularize()
        self.__assert_regular()


    def set_weight(self, u, v, new_weight):
        a, b = self.__edge2index(u, v)

        if a != None and b != None:
            self.__mat[a][b] = new_weight
        return self

    def contains_node(self, node):
        return node in self.__node2index

    def print_status(self):
        kis = [(k, v) for k, v in self.__node2index.items()]
        kis.sort(key=lambda x:x[1])

        for k, i in kis:
            print(f"key={k} -> index={i}")

        for line in self.__mat:
            print(", ".join(str(e) if e != None else "___" for e in line ))

    def storage_type(self):
        return PHY_MAT

    @staticmethod
    def from_edge_list(edges: List[Tuple]):
        g = AdjMat()
        for u, v, w in edges:
            g.add_edge(u, v, w)
        return g
