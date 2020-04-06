from unittest import TestCase

from src.Graph.graph import Graph, GraphException, PHY_ADJ_LIS
from src.Graph.weighted_adj_lis import WeightedAdjLis
from src.Graph.test_graph import GRAPH_CASES

class TestWeightedAdjLis(TestCase):

    def test_add_node(self):
        g1 = WeightedAdjLis()
        g1.add_node(1)
        assert g1.get_num_node() == 1
        assert g1.contains_node(1)

        g1.add_node(2)
        assert g1.get_num_node() == 2
        assert g1.contains_node(2)

        try:
            g1.add_node(2)
            raise Exception("Test should panic.")
        except GraphException:
            pass

    def test_add_edge(self):
        g1 = WeightedAdjLis()
        g1.add_edge(1, 2, 3)
        assert g1.get_num_edge() == 1
        assert g1.get_num_node() == 2

        g1.add_edge(2, 1, 4)
        assert g1.get_num_edge() == 2
        assert g1.get_num_node() == 2

        try:
            g1.add_edge(1, 2, 1)
            raise Exception("Test should panic.")
        except GraphException:
            pass

    def test_get_neighbour(self):
        g = WeightedAdjLis()\
            .add_edge(1, 2, 2)\
            .add_edge(2, 3, 4)\
            .add_edge(1, 3, 5)\
            .add_edge(2, 7, 3)

        n1 = g.get_neighbours(1)
        n1.sort(key=lambda x:x[0])
        assert n1 == [(2, 2), (3, 5)]

        n2 = g.get_neighbours(2)
        n2.sort(key=lambda x:x[0])
        assert n2 == [(3, 4), (7, 3)]

        assert [] == g.get_neighbours(666)

    def test_get_edge(self):
        for label, lis in GRAPH_CASES.items():
            g = WeightedAdjLis.make(lis)
            for u, v, w in lis:
                p = g.get_edge(u, v)
                assert (u, v, w) == p, \
                    f"error, test case: {label}. expected ({u}, {v}, {w}), got {p}"

    def test_delete_node(self):
        g1 = WeightedAdjLis.make(GRAPH_CASES["circle"])
        assert g1.get_num_node() == 5
        assert g1.get_num_edge() == 5

        g1.del_node(1)
        assert g1.get_num_node() == 4
        assert g1.get_num_edge() == 3

        g1.del_node(2)
        assert g1.get_num_node() == 3
        assert g1.get_num_edge() == 2

        g1.del_node(3)
        assert g1.get_num_node() == 2
        assert g1.get_num_edge() == 1

        g1.del_node(4)
        assert g1.get_num_node() == 1
        assert g1.get_num_edge() == 0

        g1.del_node(5)
        assert g1.get_num_node() == 0
        assert g1.get_num_edge() == 0

        g1.del_node(2)
        assert g1.get_num_node() == 0
        assert g1.get_num_edge() == 0

    def test_delete_edge(self):
        """
        "4-complete":[
            (1, 2, 1), (1, 3, 1), (1, 4, 1),
            (2, 1, 1,),(2, 3, 1), (2, 4, 1),
            (3, 1, 1), (3, 2, 1), (3, 4, 1),
            (4, 1, 1), (4, 2, 1), (4, 3, 1),
        ],
        :return:
        """
        g = WeightedAdjLis.make(GRAPH_CASES["4-complete"])
        assert g.del_edge(1, 2) == (1, 2, 1)
        assert g.del_edge(2, 1) == (2, 1, 1)
        assert g.get_num_edge() == 10, f"error: {g.get_num_edge()}"
        assert g.get_num_node() == 4
        assert g.del_edge(1, 2) == None

    def test_from_lis(self):
        for label, lis in GRAPH_CASES.items():
            node_set = set()
            for u, v, _ in lis:
                node_set.add(u)
                node_set.add(v)
            n = len(lis)

            g = WeightedAdjLis.make(lis)

            assert g.get_num_edge() == n
            assert g.get_num_node() == len(node_set)
            for u, v, w in lis:
                assert g.contains_node(u)
                assert g.contains_node(v)
                assert (u, v, w) == g.get_edge(u, v)

    def test_set_weight(self):
        g = WeightedAdjLis.make(GRAPH_CASES["4-complete"])

        assert (2, 1, 1) == g.get_edge(2, 1)
        assert (1, 2, 1) == g.get_edge(1, 2)

        g.set_weight(1, 2, 10).set_weight(2, 1, 666)
        assert (2, 1, 666) == g.get_edge(2, 1)
        assert (1, 2, 10) == g.get_edge(1, 2)

        assert None == g.get_edge(666, 233)
        g.set_weight(666, 233, 888)
        assert None == g.get_edge(666, 233)

    def test_nodes(self):
        def test_node(label:str, case):
            correct = set()
            for u, v, _ in case:
                correct.add(u)
                correct.add(v)
            correct = [x for x in correct]
            correct.sort()

            g = Graph.make(type=PHY_ADJ_LIS, edges=case)
            output = g.get_storage().nodes()
            output.sort()
            assert output == correct, f"Error, label={label}, output={output}"

        for label, case in GRAPH_CASES.items():
            test_node(label, case)

    def test_edges(self):
        def test_edge(label:str, case):
            cmp_closure = lambda x: (x[0], x[1], x[2])
            correct = case
            correct.sort(key=cmp_closure)

            g = Graph.make(type=PHY_ADJ_LIS, edges=case)
            output = g.get_storage().edges()
            output.sort(key=cmp_closure)
            assert output == correct, f"Error, label={label}, \noutput={output}\ncorrect={correct}"

        for label, case in GRAPH_CASES.items():
            test_edge(label, case)

    def test_transposition(self):
        def test_trans(src, tar, type):
            trans = Graph.make(PHY_ADJ_LIS, src)\
                        .get_storage()\
                        .transposition()
            cmp = Graph.make(type, tar)
            assert cmp.get_storage() == trans

        test_trans(
            GRAPH_CASES["tree"],
            [(4, 3, 1), (5, 3, 1), (6, 3, 1), (3, 2, 1), (2, 1, 1)],
            PHY_ADJ_LIS
        )

        test_trans(
            GRAPH_CASES["cyclic"],
            [(4, 2, 2), (2, 3, 1), (3, 1, 1), (1, 2, 1)],
            PHY_ADJ_LIS
        )

        test_trans(
            GRAPH_CASES["4-complete"],
            GRAPH_CASES["4-complete"],
            PHY_ADJ_LIS
        )

        test_trans(
            GRAPH_CASES["nil"],
            GRAPH_CASES["nil"],
            PHY_ADJ_LIS
        )




