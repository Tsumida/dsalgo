# 2020-02-03

from unittest import TestCase

from src.Graph.graph import WeightedAdjLis, Graph, GraphException

CASES = {
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
class TestGraph(TestCase):
    
    def test_usage(self):
        lis = CASES["tree"]
        _ = Graph()\
            .set_type(Graph.PHY_ADJ_LIS)\
            .from_list(lis)

        _ = Graph.from_edge_list(Graph.PHY_ADJ_LIS, lis)

    def test_graph_storage(self):
        lis = CASES["tree"]
        g = Graph.from_edge_list(Graph.PHY_ADJ_LIS, lis)
        sto = g.get_storage()
        assert isinstance(sto, WeightedAdjLis)


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
        for label, lis in CASES.items():
            g = WeightedAdjLis.from_edge_list(lis)
            for u, v, w in lis:
                p = g.get_edge(u, v)
                assert (u, v, w) == p, \
                    f"error, test case: {label}. expected ({u}, {v}, {w}), got {p}"

    def test_delete_node(self):
        g1 = WeightedAdjLis.from_edge_list(CASES["circle"])
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
        g = WeightedAdjLis.from_edge_list(CASES["4-complete"])
        assert g.del_edge(1, 2) == (1, 2, 1)
        assert g.del_edge(2, 1) == (2, 1, 1)
        assert g.get_num_edge() == 10, f"error: {g.get_num_edge()}"
        assert g.get_num_node() == 4
        assert g.del_edge(1, 2) == None


    def test_from_lis(self):
        for label, lis in CASES.items():
            node_set = set()
            for u, v, _ in lis:
                node_set.add(u)
                node_set.add(v)
            n = len(lis)

            g = WeightedAdjLis.from_edge_list(lis)

            assert g.get_num_edge() == n
            assert g.get_num_node() == len(node_set)
            for u, v, w in lis:
                assert g.contains_node(u)
                assert g.contains_node(v)
                assert (u, v, w) == g.get_edge(u, v)

    def test_set_weight(self):
        g = WeightedAdjLis.from_edge_list(CASES["4-complete"])

        assert (2, 1, 1) == g.get_edge(2, 1)
        assert (1, 2, 1) == g.get_edge(1, 2)

        g.set_weight(1, 2, 10).set_weight(2, 1, 666)
        assert (2, 1, 666) == g.get_edge(2, 1)
        assert (1, 2, 10) == g.get_edge(1, 2)

        assert None == g.get_edge(666, 233)
        g.set_weight(666, 233, 888)
        assert None == g.get_edge(666, 233)

