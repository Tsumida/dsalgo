import sys
sys.setrecursionlimit(4096)

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # x in [0, m), y in [0, n)
        def is_valid(x:int, y:int) -> bool:
            if x >= m or y >= n or x < 0 or y < 0:
                return False
            s = 0
            while x > 0:
                s += x % 10
                x = x // 10
            while y > 0:
                s += y % 10
                y = y // 10
            #print("ok:", x, y, s)
            return s <= k

        def dfs(x:int, y:int):
            # 从[0, 0]开始
            if (x, y) in is_reachable:
                return
            is_reachable.add((x, y))
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if is_valid(i, j):
                    dfs(i, j)

        is_reachable = set()
        dfs(0, 0)
        res = len(is_reachable)
        #print(res)
        #print(is_reachable)
        return res

s = Solution()
assert 3 == s.movingCount(m = 2, n = 3, k = 1)
assert 1 == s.movingCount(m = 3, n = 1, k = 0)
s.movingCount(m = 20, n = 100, k = 20)
