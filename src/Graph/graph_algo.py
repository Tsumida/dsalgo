# 2020-02-03
from src.Graph.graph_storage import *
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
            if cyclic_flag:
                break
            if color[node] == WHITE:
                dfs(node)

        return not cyclic_flag

    def is_connected(self, graph: Graph) -> bool:
        return False

    def topological_sort_recur(self, graph: Graph) -> (bool, list):
        def dfs(node) -> bool:
            c = is_visited[node]
            flag = True
            if c == UNVISITED:
                is_visited[node] = VISITING
                for v, _ in sto.get_neighbours(node): # 返回的是(v, weight)
                    status = is_visited[v]
                    if status == VISITING: return False
                    if status != UNVISITED: continue
                    flag = flag and dfs(v)
                    is_visited[v] = VISITED
                    if not flag:
                        cycle.append(v)
                        break
                is_visited[node] = VISITED
                tmp.append(node)
                return flag
            return True

        UNVISITED, VISITING, VISITED = 0, 1, 2
        res = []
        tmp = []
        cycle = []
        is_visited = dict()
        sto = graph.get_storage()
        nodes = sto.nodes()
        f = True
        for n in nodes:
            is_visited[n] = UNVISITED
        for n in nodes:
            f = f and dfs(n)
            if not f:
                cycle.append(n)
                print(f"Error, cycle: {cycle}")
                res.clear()
                break
            if len(tmp) > 0:
                res.extend(reversed(tmp))
                tmp.clear()
        res.reverse()
        return f, res

    def cal_finish_time(self, graph: Graph):
        """
        time: O(V+E)
        Computing finishing time for each node, sort them in decreasing order.
        :param graph:
        :return:
        """
        def dfs(u):
            if u not in is_visited:
                is_visited.add(u)
                for v, _ in sto.get_neighbours(u):
                    dfs(v)
                result.append(u)

        is_visited = set()
        result = []
        sto = graph.get_storage()
        for node in sto.nodes():
            dfs(node)
        # print("result = ", result)
        return result

    def scc(self, graph: Graph):
        """
        Get strong connected components.
        :return: List[List[node_label]]
        """

        sto = graph.get_storage()
        finish_time = self.cal_finish_time(graph)
        finish_time.reverse() # 按finish_time 降序
        print(finish_time)
        trans = sto.transposition()
        st = []
        res = []
        tmp = []
        is_visited = set()
        for node in finish_time:
            # 在同一个dfs森林的点都放入了tmp
            if node in is_visited:
                continue
            st.append(node)
            while len(st) > 0:
                nod = st.pop()
                if nod in is_visited:
                    continue
                tmp.append(nod)
                is_visited.add(nod)
                for v, _ in trans.get_neighbours(nod):
                    st.append(v)
            res.append(tmp.copy())
            print(st, is_visited, tmp)
            st.clear()
            tmp.clear()
        print("res=", res)
        return res













