from src.Graph.graph import *

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
        # O(V)
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
        # O(1)
        # 删除边并返回
        a, b = self.__edge2index(u, v)
        if a != None and b != None:
            val = self.__mat[a][b]
            if val:
                self.__mat[a][b] = None
                return u, v, val
        return None

    def contains_edge(self, u, v):
        # O(1)
        # 判断是否包含一条边(u, v)
        a, b = self.__edge2index(u, v)
        return a != None and b != None and self.__mat[a][b]

    def get_neighbours(self, node):
        # O(E)
        # 获得点所有的出边, 类型是 (node, weight)
        # usage: for v, w in graph.get_neighbours("z city")
        a = self.__node2index.get(node, None)
        if a != None:
            return [(self.__index2node[i], v) for i, v in enumerate(self.__mat[a]) if v != None]
        else:
            return list()

    def add_node(self, node):
        # O(V)
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
        # O(V^2)
        # 删除所有与node关联的边
        self.__assert_regular()
        index = self.__node2index.get(node, None)
        if index != None:
            self.__mat[index] = None # 标记node的行为None
            self.__regularize()
        self.__assert_regular()

    def set_weight(self, u, v, new_weight):
        # O(1)
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

    def nodes(self):
        # O(V)
        return [label for label in self.__node2index.keys()]

    def edges(self):
        # O(V^2)
        n = len(self.__node2index)
        res = []
        for i in range(n):
            for j in range(n):
                weight = self.__mat[i][j]
                if weight != None:
                    res.append((self.__index2node[i], self.__index2node[j], weight))
        return res

    @staticmethod
    def make(edges: List[Tuple]):
        g = AdjMat()
        for u, v, w in edges:
            g.add_edge(u, v, w)
        return g

    def transposition(self):
        raise GraphException("Unimplemented!")
