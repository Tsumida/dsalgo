class Solution:
    def fib(self, n: int) -> int:

        MOD = (10 ** 9) + 7
        dp = [0, 1, 1]
        for i in range(3, n+1):
            num = (dp[-1] + dp[-2]) % MOD
            dp.append(num)

        return dp[n]

s = Solution()
assert 1 == s.fib(n=2)
assert 1 == s.fib(n=1)
assert 0 == s.fib(n=0)
