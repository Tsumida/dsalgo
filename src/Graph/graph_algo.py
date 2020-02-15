# 2020-02-03
from src.Graph.graph import *

class GraphAlgo:
    def __init__(self):
        pass

    def mat_to_adj_lis(self, graph: Graph):
        pass

    def adj_lis_to_mat(self, graph: Graph):
        pass

    def is_acyclic(self, graph: Graph) -> bool:
        def dfs(u):
            nonlocal cyclic_flag
            color[u] = GRAY
            neighbours = sto.get_neighbours(u)
            for nod, _ in neighbours:
                c = color[nod]
                if c == WHITE:
                    dfs(nod)
                elif c == GRAY or cyclic_flag:
                    cyclic_flag = True
                    break
            color[u] = BLACK  # 所有经过的点都会变为黑色

        WHITE, GRAY, BLACK = 0, 1, 2 # unvisited, visiting, visited
        sto = graph.get_storage()
        nodes = sto.nodes()
        color = dict()
        for u in nodes:
            color[u] = WHITE

        cyclic_flag = False
        for node in nodes:
            if color[node] == WHITE and not cyclic_flag:
                dfs(node)

        return not cyclic_flag

    def is_connected(self, graph: Graph) -> bool:
        return False

    def topological_sort(self, graph: Graph) -> bool:
        pass














