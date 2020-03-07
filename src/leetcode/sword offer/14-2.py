class Solution:
    def cuttingRope(self, n: int) -> int:
        # 贪心算法
        # 考虑: 2 * dp(n-2), 3 * dp(n-3)
        # 因为n>=5 时， 必有 2(n-2) > 5 and 3(n-3) > n
        assert n > 1
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4

        res = 0
        # 因为n>=5时, 3(n-3) >= 2(n-2)
        step = n // 3
        left = n % 3 # 0, 1, 2

        if left == 1:
            step -= 1 # 剩下1时，再拿个3凑成4
            res = (3 ** step) << 2
        elif left == 2:
            res = (3 ** step) << 1
        else:
            res = (3 ** step)
        # 考虑分为2
        return res % (10 ** 9 + 7)

s = Solution()
assert 1 == s.cuttingRope(n=2)
assert 2 == s.cuttingRope(n=3)
assert 6 == s.cuttingRope(n=5)
assert 36 == s.cuttingRope(n=10)
assert 81 == s.cuttingRope(n=12)
