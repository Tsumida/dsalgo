# 2020-1-2

from typing import List

class Solution:
    # 题解1: 思路是降序排序 + 图形化解法:
    # 寻找第一个i使得 citation[i] > i => res = i + 1
    def hIndex(self, citations: List[int]) -> int:
        hmap = dict()
        res = 0
        citations.sort(reverse=True)
        for i, p in enumerate(citations):
            hmap[p] = i+1 # i+1个不小于p的元素
        #print(hmap)
        for p, num in hmap.items():
            res = max(res, min(p, num))
        #print(citations, res)

        return res

s = Solution()
assert 3 == s.hIndex(citations=[3, 0, 6, 1, 5])
assert 2 == s.hIndex(citations=[1, 2, 3, 1, 1])
assert 3 == s.hIndex(citations=[2, 4, 4, 5])
assert 3 == s.hIndex(citations=[2, 1, 1, 1, 4, 4, 4]) # 3
assert 3 == s.hIndex(citations=[3, 3, 3, 1]) # 3
assert 1 == s.hIndex(citations=[1]) # 1
assert 1 == s.hIndex(citations=[100]) # 1
assert 4 == s.hIndex(citations=[5, 5, 5, 5]) # 4
assert 0 == s.hIndex(citations=[]) # 0
