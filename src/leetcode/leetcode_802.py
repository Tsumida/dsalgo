# 2018-12-21

# leetcode_802
# passed - 2018-12-27

import collections

class Solution:

    Unknown = 0
    Safe = 1
    Unsafe = -1

    Gray = 1
    White = 0
    Black = -1

    # 若dfs -> False, 则
    def dfs(self, index, adj_list, color, status) -> bool:
        flag = True
        if color[index] == self.Gray:
            flag = False
        elif color[index] == self.White: # Unknown
            # use v in adj[index] to
            color[index] = self.Gray
            # 对每个v 进行dfs
            for v in adj_list[index]:
                # 如果相邻点有一个是不安全的，就是不安全的
                if (self.dfs(v, adj_list, color, status) == False):
                    status[index] = self.Unsafe
                    flag = False
                    #不要break

            if status[index] == self.Unknown:
                status[index] = self.Safe
                for v in adj_list[index]:   # 如果有一个不安全，index就是不安全
                    if status[v] == self.Unsafe:
                        status[index] = self.Unsafe

            color[index] = self.Black
        else: # Black
            pass

        print(f"------- index - {index}")
        for c in status:
            print(c, end=" ")
        print("\n")

        return flag


    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        lens = len(graph)
        res = []

        color = [self.White for i in range(lens)]
        status = [self.Unknown for i in range(lens)]
        for u in range(lens):
            self.dfs(u, graph, color, status)
        res = [i for i in range(lens) if status[i] == self.Safe]
        return res





    def test(self):
        case_1 = [[1,2],[2,3],[5],[0],[5],[],[]]        # passed
        case_2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]       # passed

        case_3 = [
            [1],[2],[3],[4],[0], # 环
            [4],[3],[2],[1],[0]
        ]

        res_1 = self.eventualSafeNodes(case_2)
        print(res_1)
        # ans_1 = [2, 4 ,5, 6]

class Solution_fastest:
    def eventualSafeNodes(self, graph):
        """
        同上，这次采用深度优先搜索的方法解决问题
        :param graph:
        :return:9
        """
        WHITE,GRAY,BLACK=0,1,2
        color=collections.defaultdict(int)
        def dfs(node):
            if color[node]!=WHITE:
                return color[node]==BLACK
            color[node]=GRAY
            for nei in graph[node]:
                if color[nei]==BLACK:
                    continue
                if color[nei]==GRAY or not dfs(nei):
                    return False
            color[node]=BLACK
            return True
        return list(filter(dfs,range(len(graph))))

if __name__ == "__main__":
    s1 = Solution()
    s1.test()
