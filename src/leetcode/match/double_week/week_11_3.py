# 2019-10-19

'''
5090. 抛掷硬币 显示英文描述

有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。

请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。
'''
class Solution:
    def probabilityOfHeads(self, prob: list, target: int) -> float:
        res = 0.0
        n = len(prob)
        # dp ?
        dp = [[0.0 for k in range(n)] for q in range(target)]
        # dp[q, k] 表示从 [0, k] 中取出 0 <= q <= k 个正面的概率

        return res

s = Solution()
assert 0.40 == s.probabilityOfHeads(prob=[0.4], target=1)
assert 0.03125 == s.probabilityOfHeads(prob=[0.5,0.5,0.5,0.5,0.5], target=0)

