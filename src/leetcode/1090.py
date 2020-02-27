# 2020-02-06

from typing import List

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        if num_wanted == 0 or use_limit == 0:
            return 0

        res = 0
        cnt = 0
        tmp = []
        check_map = dict()
        n = len(values)
        assert n == len(labels)
        for i in range(n):
            tmp.append((values[i], labels[i]))

        tmp.sort(reverse=True, key=lambda x: x[0])

        for v, l in tmp:
            p = check_map.get(l, 0)
            if p < use_limit:
                check_map[l] = p + 1
                cnt += 1
                res += v
            if cnt >= num_wanted:
                break
        print(res)
        return res

s = Solution()
assert 9 == s.largestValsFromLabels(values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1)
assert 12 == s.largestValsFromLabels(values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2)
assert 16 == s.largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1)
assert 24 == s.largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2)
assert 0 == s.largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 0)
assert 12 == s.largestValsFromLabels(values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 3)
assert 20000 == s.largestValsFromLabels(values=[1] * 20000, labels=[2] * 20000,  num_wanted=20000, use_limit=20000)
