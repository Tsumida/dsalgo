from abc import ABC
from typing import List, Tuple


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
        """
        Return all nodes.
        :return:
        """
        pass

    def edges(self):
        pass

    @staticmethod
    def make(edges:List[Tuple]):
        pass

    def transposition(self):
        pass
