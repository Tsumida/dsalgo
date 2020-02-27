# leetcode 714
#

class Solution:
    # len(prices) <= 50, 000
    # 无限次交易, 每次要收取 fee 费用
    # 与122不同的是, 每次收取fee可能把多次sell变为一次：
    # 1  5 4 8 -->  8 - 4 - 2 = 2, 5 - 1 - 2 = 2 --> 4
    # 但是更短的是 8 - 1 - 2 = 5
    def maxProfit(self, prices: list, fee: int) -> int:
        res = 0
        i = len(prices) - 1
        while i > 0:
            res += max(0, prices[i] - prices[i-1] - fee)
            i -= 1

        print(fee, prices, res)
        return res


s = Solution()

assert 8 == s.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2)
assert 0 == s.maxProfit(prices=[1], fee=100)          # 不买
assert 0 == s.maxProfit(prices=[1, 2], fee=1)
assert 5 == s.maxProfit(prices=[1, 5, 4, 8], fee=2)   # 多笔带来的收益小于一笔
assert 0 == s.maxProfit(prices=[1, 5, 4, 8], fee=200) # fee超过最大收益， 不买是最优选择
assert 0 == s.maxProfit(prices=[1]*1000, fee=1)
assert 1 == s.maxProfit(prices=[i for i in range(100)], fee=1)
