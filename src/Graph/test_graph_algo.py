from unittest import TestCase

from src.Graph.graph import Graph, PHY_ADJ_LIS, PHY_MAT
from src.Graph.graph_algo import GraphAlgo
from src.Graph.test_graph import GRAPH_CASES

class TestGraphAlgo(TestCase):
    def test_is_acyclic(self):
        def test_case(label:str, case, ans:bool):
            algo = GraphAlgo()
            g_lis = Graph.make(type=PHY_ADJ_LIS, edges=case)
            g_mat = Graph.make(type=PHY_MAT, edges=case)
            assert ans == algo.is_acyclic(g_lis), f"fail, label:{label}"
            assert ans == algo.is_acyclic(g_mat), f"fail, label:{label}"

        test_case("tree", GRAPH_CASES["tree"], True)
        test_case("dag", GRAPH_CASES["dag"], True)

        test_case("cyclic", GRAPH_CASES["cyclic"], False)
        test_case("4-complete", GRAPH_CASES["4-complete"], False)
