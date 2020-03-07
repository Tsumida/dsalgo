class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        assert n > 0 # 负数会导致死循环，要注意逻辑右移和算术右移
        while n > 0:
            if n % 2 == 1:
                res += 1
            n = n >> 1
        #print(res)
        return res

s = Solution()
assert 0 == s.hammingWeight(n=0)
assert 1 == s.hammingWeight(n=1)
assert 2 == s.hammingWeight(n=3)
assert 3 == s.hammingWeight(n=7)
assert 1 == s.hammingWeight(n=16)
assert 1 == s.hammingWeight(n=1 << 10)
assert 10 == s.hammingWeight(n=1023)
assert 3 == s.hammingWeight(n=56)
