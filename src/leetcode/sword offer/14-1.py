class Solution:
    # 有贪心解法， 见
    # https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
    def cuttingRope(self, n: int) -> int:
        record = {
            1: 1,
            2: 1,
            3: 2, # 1, 2 或者 2, 1
        }
        for i in range(4, n+1):
            tmp = 0
            for j in range(1, i):
                p = record[j] * (i-j)
                # 因为record[j]至少两端，所以p代表分为至少3段时的最大值
                # (i-j)*j 代表分为两端的最大值
                tmp = max(max(tmp, p), (i-j)*j)
                #print(i, tmp)
            record[i] = tmp
        print(record[n])
        return record[n]

s = Solution()
assert 1 == s.cuttingRope(n=1)
assert 1 == s.cuttingRope(n=2)
assert 2 == s.cuttingRope(n=3)
assert 36 == s.cuttingRope(n=10)
assert 81 == s.cuttingRope(n=12)
