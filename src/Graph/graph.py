# 2020-02-03

from src.Graph.weighted_adj_lis import *
from src.Graph.adj_mat import *
from src.Graph.others import *

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



