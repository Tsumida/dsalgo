

from math import sqrt

class Solution:
    def divisorGame(self, N: int) -> bool:
        """
        dp[m] == 0 ---> 未
        dp[m] == 1 ---> 若alice 2k+1 到达这个点， 会赢

        :param N:
        :return:
        """
        def dfs(M:int, p:int):
            res = 0

            if dp[M] != 0:
                res = dp[M]
            else:
                sqrt_m = sqrt(M) + 1
                for factor in range(1, int(sqrt_m+1)):
                    if M % factor == 0:
                        res = dfs(M-factor, p+1)
                        break


        dp = [0 for x in range(N+1)]
        dp[0] = -1 # 不可以
        dp[1] = -1
        dp[2] = 1

        result = 0
        # alice == 2k+1
        result = dfs(N, 1)
        if p % 2 == 0: # Bob
            res = -1 * res


        return dp[N]

strs = "%E8%82%A5%E4%BB%94%E4%B8%AA%E5%A4%B4"

print(strs)
