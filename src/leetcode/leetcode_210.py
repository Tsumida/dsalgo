# 2018-12-1
# leetcode 210


# 思路：建立邻接表， 做拓扑排序
from collections import deque

class Solution:
    GRAY = 0        # during searching
    WHITE = 1       # unvisited
    BLACK = -1      # visited

    def findOrder(self, numCourses, prerequisites) -> list:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # color
        color = [self.WHITE for i in range(numCourses)]

        # create adj_list
        adj_list = [ [] for i in range(numCourses)]
        for edge in prerequisites:
            u, v = edge # (0, 1) 表示要学习1必须要先学习0
            adj_list[v].append(u)

        # topological
        result_deque = deque()
        for i in range(numCourses):
            path = []
            if self.topological_sort(adj_list, color, i, path) == True:
                # 要把结果逆转
                for e in path:
                    result_deque.appendleft(e)
            else : # 有环， 清空result
                result_deque.clear()
                break
        result = list(result_deque)
        return  result

    def topological_sort(self, adj_list, color, node_index, path) -> bool:
        # 递归：   对每个白色节点涂成GRAY， 再做dfs. 若节点本来是灰色， 就返回
        # 边界:    如果在次过程中， 碰到GRAY节点，就断定有环， 返回False， 说明不能产生线序
        #                若是BLACK， 则跳过
        #         若到了尽头，无环，则返回True， 同时把本层（node_index)压入path中， 返回True
        # 递归:    返回某层， 若返回True，表明把本层node_index压入path
        res = True
        if color[node_index] == self.WHITE:
            color[node_index] = self.GRAY
            # len(adj(node_index)) = 0 is ok too.
            for v in adj_list[node_index]:
                if self.topological_sort(adj_list, color, v, path) == False: # Cyclic
                    res = False
                    break
            path.append(node_index) # 先递归后压入
            color[node_index] = self.BLACK  # this node was already visited.

        elif color[node_index] == self.GRAY: # GRAY node
            res = False
        # search will skip BLACK node.

        return res

def test(s):
    case_1 = (4, [[1,0],[2,0],[3,1],[3,2]])
    case_2 = (2, [[1,0]] )                          # 要学1， 必须先学0
    case_2_2 = (2, [[0,1]] )                        # res = [1, 0]
    case_3 = (4, [[1, 0], [0, 3], [3, 2], [2, 1]])  # 环
    case_4 = (4, [])                                # 空

    print(s.findOrder(case_1[0], case_1[1]))
    print(s.findOrder(case_2[0], case_2[1]))
    print(s.findOrder(case_2_2[0], case_2_2[1]))
    print(s.findOrder(case_3[0], case_3[1]))
    print(s.findOrder(case_4[0], case_4[1]))

if __name__ == "__main__":
    s = Solution()
    test(s)
