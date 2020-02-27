# 2019-6-1

"""
class Solution:
    def indexPairs(self, text: str, words: list) -> list:
        res = list()

        for word in words:
            index = 0
            lens = len(text)
            while index < lens:
                first_index = text.find(word, index) # [index, lens)
                if first_index != -1:
                    res.append((first_index, first_index+len(word)-1))
                index += 1

        #res.sort(key=lambda ele: (ele[0], ele[1]))
        res = [x for x in set(res)]
        res.sort(key=lambda  ele: (ele[0], ele[1]))

        return res
s = Solution()
print(s.indexPairs(text="ababa", words=["aba","ab"]))
"""

class Solution:
    def assignBikes(self, workers: list, bikes: list) -> int:
        def mdist(w:list, b:list) -> int:
            return abs(w[0] - b[0]) + abs(w[1] - b[1])

        def is_legal(x:int, y:int) -> bool:
            res = False
            if not row_dect[x] and not col_dect[y]:
                row_dect[x] = True
                col_dect[y] = True
                res = True

            return res

        def reset(x:int, y:int):
            row_dect[x] = False
            col_dect[y] = False

        def search(worker:int, bound:int) -> int:

            temp = bound
            if worker < n:
                temp = INF
                for bike in range(m):
                    if is_legal(worker, bike):
                        # 令worker选取bike
                        # 从search结果中找最小的一个
                        temp = min(temp, search(worker+1, bound + mdists[worker][bike]))
                        #print("worker=", worker,"---"*worker, "temp=", temp, "\nbike=", bike)
                        reset(worker, bike)

            return temp


        # 这厮应该是八皇后的变种

        INF = 1 << 24
        res = INF
        n, m = len(workers), len(bikes) # n <= m
        bound = 0
        mdists = [
            [mdist(workers[i], bikes[j]) for j in range(m)] for i in range(n)
        ]

        # 用来快速判断是否可行
        row_dect, col_dect = [False for x in range(n)], [False for x in range(m)]

        # 搜索
        res = min(res, search(0, 0))

        return res


s = Solution()
print(s.assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]],
                    [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999]]))
