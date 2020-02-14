# 2020-02-03
from unittest import TestCase
from src.Graph.graph import *
from src.Graph.test_graph import GRAPH_CASES

class GraphAlgo:
    def __init__(self):
        pass

    def mat_to_adj_lis(self, graph: Graph):
        pass

    def adj_lis_to_mat(self, graph: Graph):
        pass

    def is_acyclic(self, graph: Graph) -> bool:
        def dfs(node):
            pass


        sto = graph.get_storage()
        is_visited = set()


    def is_connected(self, graph: Graph) -> bool:
        return False

    def topological_sort(self, graph: Graph) -> bool:
        pass

class TestGraphAlgo(TestCase):
    def test_is_acyclic(self):
        def test_case(label:str, case):
            algo = GraphAlgo()
            g_lis = Graph.make(type=PHY_ADJ_LIS, edges=case)
            g_mat = Graph.make(type=PHY_MAT, edges=case)
            assert algo.is_acyclic(g_lis), f"fail, label:{label}"
            assert algo.is_acyclic(g_mat), f"fail, label:{label}"

        for label, case in GRAPH_CASES.items():
            test_case(label, case)











