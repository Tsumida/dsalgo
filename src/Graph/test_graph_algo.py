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

    def test_topo_sort_recur(self):
        g1 = Graph.make(type=PHY_ADJ_LIS, edges=GRAPH_CASES['tree'])
        g1m = Graph.make(type=PHY_MAT, edges=GRAPH_CASES['tree'])

        algo = GraphAlgo()
        flag, lis = algo.topological_sort_recur(g1)
        assert flag
        flag, lis = algo.topological_sort_recur(g1m)
        assert flag

        g1 = Graph.make(type=PHY_ADJ_LIS, edges=GRAPH_CASES['circle'])
        g1m = Graph.make(type=PHY_MAT, edges=GRAPH_CASES['circle'])
        flag, lis = algo.topological_sort_recur(g1)
        assert not flag
        flag, lis = algo.topological_sort_recur(g1m)
        assert not flag

        g1 = Graph.make(type=PHY_ADJ_LIS, edges=GRAPH_CASES['dag'])
        g1m = Graph.make(type=PHY_MAT, edges=GRAPH_CASES['dag'])
        flag, lis = algo.topological_sort_recur(g1)
        assert flag
        # print(lis)
        flag, lis = algo.topological_sort_recur(g1m)
        assert flag
        # print(lis)

    def test_scc(self):
        g1 = Graph.make(PHY_ADJ_LIS, GRAPH_CASES["tree"])
        res = GraphAlgo().scc(g1)
        print(res)

        g2 = Graph.make(PHY_ADJ_LIS, GRAPH_CASES["cyclic"])
        res = GraphAlgo().scc(g2)
        print(res)

        g3 = Graph.make(PHY_ADJ_LIS, GRAPH_CASES["4-complete"])
        res = GraphAlgo().scc(g3)
        print(res)
