# 2019-9-24
class Solution:

    def domino(self, n: int, m: int, broken: list) -> int:
        # count <= n*m-1
        # 返回下一个空白格的坐标
        def get_next_ord(count: int):
            if count <= LIMIT:
                x, y = count // m, count % m
                #print(x, y)
                while not chess[x][y]:
                    # 从左往右v
                    y += 1
                    if y >= m:
                        x += 1
                        y = 0
                    if x >= n:
                        x, y = -1, -1
                        break

                return (x, y)
            else:
                return (-1, -1)

        # prev_num是上一层发现的最大的覆盖数
        def search(count: int, prev_num:int) -> int:
            if count > LIMIT:
                return prev_num
            x, y = get_next_ord(count)
            result = prev_num
            nonlocal stime
            stime += 1
            if chess[x][y]:
                #print("Searching: ", x, y, prev_num, count)
                chess[x][y] = False
                if y+1< m and chess[x][y+1]:
                    chess[x][y+1] = False
                    result = max(result, search(count+1, prev_num+1)) # 放下一个覆盖
                    chess[x][y+1] = True
                if x+1< n and chess[x+1][y]:
                    chess[x+1][y] = False
                    result = max(result, search(count+1, prev_num+1))
                    chess[x+1][y] = True
                chess[x][y] = True

            # print("search result: ", result)
            return result

        res = 0
        if n <= 1 or m <= 1:
            return res
        # n行m列矩阵上有 一些坏掉的格子(Broken)
        # 搜索 + 回溯 + 剪枝
        # 有横着放\ 竖着放两种
        #print(n, m, broken)

        chess = [[True for _ in range(m)] for _ in range(n)] # T 表示没被覆盖

        if broken:
            for x, y in broken:
                chess[x][y] = False
            # 对于(x, y) 检查右\下是否有空
            # 用一个计数器， 得到..坐标
            cnt = 0
            LIMIT = n*m - 1
            stime = 0
            #while cnt <= LIMIT:
                #res = max(res, search(count=cnt, prev_num=0)) # if chess[0][0] == False, stop. -> res = 0
                #cnt += 1
            res = search(count=0, prev_num=0)
            #print("res = ", res)

            print("Search time: ", stime)
        else:
            res =
        return res

    def SearchChess(self, n:int, m:int, broken: list) -> int:
        def next_x(x:int, y:int) -> int:
            next = x+1
            while next < n and not chess[next][y]:
                next += 1
            return next

        def next_y(x:int, y: int) -> int:
            next = y+1
            while next < m and not chess[x][next]:
                next += 1
            return next
        def next_dig(x:int, y:int) -> (int, int):
            return (x+1, y+1)


        def search(prev_x:int, prev_y:int, prev_res:int) -> int:
            result = prev_res
            x, y = 0, 0
            if chess[prev_x][prev_y]:
                x = next_x(prev_x, prev_y)
                if x < n and chess[x][prev_y]:
                    chess[x][prev_y] = False
                    result = max(result, search(x, prev_y, prev_res+1))
                    chess[x][prev_y] = True

                y = next_y(prev_x, prev_y)
                if y < m and chess[prev_x][y]:
                    chess[prev_x][y] = False
                    result = max(result, search(prev_x, y, prev_res+1))
                    chess[prev_x][y] = True



            return result


        res = 0
        chess = [[True for _ in range(m)] for _ in range(n)] # T 表示没被覆盖

        for x, y in broken:
            chess[x][y] = False



        return res


s = Solution()
assert 4 == s.domino(n = 3, m = 3, broken = [])
assert 2 == s.domino(n = 2, m = 3, broken = [[1, 0], [1, 1]])
assert 6 == s.domino(n = 4, m = 3, broken=[])
assert 1 == s.domino(n=2, m=2, broken=[[0, 0]])
assert 20 == s.domino(n=5, m=8, broken=[])
assert 16 == s.domino(n=6, m=6, broken=[[0, 0], [0,1], [1, 0], [1, 1]])
assert 0 == s.domino(n=2, m=2, broken=[[1, 1], [0, 0]])
assert 6 == s.domino(n=4, m=4, broken=[[0, 0], [0, 3], [3, 0], [3, 3]])
print(s.domino(n=8, m=6, broken=[]))
