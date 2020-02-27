# 2018-11-29
# 方法：输入的图G必定有且只有一个回路，输出回路中最后一条边

# 核心：找出回路的边
# 性质：G是由树生成的，则每个节点只有一个

class Solution:

    WHITE = 0
    GRAY = 1
    STATUS = 1 # == 0 dicates do not append node_index

    def findRedundantConnection(self, edges) -> list:
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        num_nodes = len(edges)+1 #从1开始
        res = []
        adj_list = [[] for i in range(num_nodes)]
        color = [self.WHITE for i in range(num_nodes)]
        #ring = []

        # create adj_list
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        # dfs
        path = set()
        for i in range(1, num_nodes):
            #print(color)
            if color[i] == self.WHITE:
                #print(color)
                path.clear()
                ring_tail = -1
                isINCycle, ring_tail = self.dfs(adj_list, i, color, -1, path, ring_tail)
                #print(path)
                if isINCycle:
                    # path.append(i)
                    break

        # process
        for edge in reversed(edges):
            if edge[0] in path:
                if edge[1] in path:
                    res.append(edge[0])
                    res.append(edge[1])
                    break
            elif edge[1] in path:
                if edge[0] in path:
                    res.append(edge[1])
                    res.append(edge[0])
                    break

        return res

    def dfs(self, adj_list, node_index, color, pred, path, ring_tail) -> ( ):

        isInCycle = False
        color[node_index] = self.GRAY # 染色

        for v in adj_list[node_index]:

            if v == pred:
                continue
            else:
                if color[v] == self.WHITE:
                    isInCycle, ring_tail = self.dfs(adj_list, v, color, node_index, path, ring_tail)

                else:
                    isInCycle = True # 碰到环了
                    ring_tail = v
                    #path.add(v)      # 保存尾巴
                if isInCycle: # 保证path[0] 必定存在
                    # path.add(node_index) 的条件是
                    # node_index ！= tail and STATUS = 1
                    #if node_index != ring_tail and self.STATUS:
                    if  self.STATUS == 1:
                        path.add(node_index)
                    if node_index == ring_tail:
                        self.STATUS = 0 # 以后的点不用push了
                    # print(f"{path} -- tail = {ring_tail} -- STATUS: -- {self.STATUS}")
                    break

        return (isInCycle, ring_tail)




    def test(self):
        case_1 = [[1,2], [1,3], [2,3]]
        case_2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
        case_3 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
        case_4 = [[1,3],[3,4],[1,5],[3,5],[2,3]]
        case_5 = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
        case_6 = [[1, 2], [2, 3], [3, 4], [3, 5], [4, 6], [4,7],[7, 8], [8, 5], [5, 9]]
        #print(self.findRedundantConnection(case_1))
        #print(self.findRedundantConnection(case_2))
        #print(self.findRedundantConnection(case_3))
        #print(self.findRedundantConnection(case_4))
        # 这个case 展示了问题，正确的路径应该是 [3, 5, 8, 7, 4, 3, #2, #1]
        print(self.findRedundantConnection(case_5))
        #self.findRedundantConnection(case_1)


s1 = Solution()
s1.test()


