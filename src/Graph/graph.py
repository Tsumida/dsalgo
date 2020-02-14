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
            self.__storage = WeightedAdjLis.make(lis)
        elif self.__type == PHY_MAT:
            self.__storage = AdjMat.make(lis)
        else:
            raise GraphException(ERR_INVALID_STORAGE_TYPE.format(self.__type))
        return self

    @staticmethod
    def make(type, edges:List[Tuple]):
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

    def nodes(self):
        pass

    def edges(self):
        pass

    @staticmethod
    def make(edges:List[Tuple]):
        pass


