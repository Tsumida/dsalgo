# 2020-02-03

from unittest import TestCase

from src.Graph.graph import Graph, PHY_MAT, PHY_ADJ_LIS
from src.Graph.weighted_adj_lis import WeightedAdjLis
from src.Graph.adj_mat import AdjMat

GRAPH_CASES = {
        "nil":[],
        "tree": [
            (1, 2, 1), (2, 3, 1), (3, 4, 1), (3, 5, 1), (3, 6, 1),
        ],
        "circle":[
            (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 2), (5, 1, 1),
        ],
        "dag":[
            (2, 7, 1), (2, 4, 1), (2, 6, 1), (2, 5, 1),
            (7, 1, 1), (7, 3, 1),
            (1, 3, 1),
            (4, 3, 1),
            (6, 5, 1),
        ],
        "cyclic":[
            (2, 1, 1), (1, 3, 1), (3, 2, 1), (2, 4, 2),
        ],
        "4-complete":[
            (1, 2, 1), (1, 3, 1), (1, 4, 1),
            (2, 1, 1,),(2, 3, 1), (2, 4, 1),
            (3, 1, 1), (3, 2, 1), (3, 4, 1),
            (4, 1, 1), (4, 2, 1), (4, 3, 1),
        ],
    }

Citys = [
    ("A city", "B city", 2.2),
    ("A city", "C city", 1.3),
    ("A city", "D city", 4.5),
    ("B city", "D city", 3.2),
    ("C city", "F city", 10.7),
    ("F city", "E city", 20.1),
    ("E city", "B city", 4.9),
]

class TestGraph(TestCase):

    def test_usage(self):
        lis = GRAPH_CASES["tree"]
        _ = Graph().set_type(PHY_ADJ_LIS).from_list(lis)
        _ = Graph.make(PHY_ADJ_LIS, lis)

        _ = Graph().set_type(PHY_MAT).from_list(lis)
        _ = Graph.make(PHY_MAT, lis)

    def test_graph_storage(self):
        lis = GRAPH_CASES["tree"]
        g = Graph.make(PHY_ADJ_LIS, lis)
        sto = g.get_storage()
        assert isinstance(sto, WeightedAdjLis)

        g2 = Graph.make(PHY_MAT, lis)
        sto2 = g2.get_storage()
        assert isinstance(sto2, AdjMat)

    def test_city(self):
        g1 = Graph.make(PHY_MAT, Citys)
        g2 = Graph.make(PHY_ADJ_LIS, Citys)

        g1.get_storage().print_status()
        print("-"*32)
        g2.get_storage().print_status()

