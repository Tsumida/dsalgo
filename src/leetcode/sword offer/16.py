class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = self.method_quick_power(x, n)
        if n < 0:
            res = 1 / res
        print(res)
        return res

    def method_quick_power(self, x: float, n: int) -> float:
        assert x != 0
        abs_n = abs(n)
        if abs_n == 0:
            return 1.0
        elif abs_n == 1:
            return x
        else:
            abs_n = abs(n)
            tmp = self.method_quick_power(x, abs_n >> 1) ** 2
            if abs_n % 2 == 1:
                tmp *= x
            return tmp


s = Solution()
assert 1.0 == s.myPow(x=1.0, n=10)
assert 4.0 == s.myPow(x=2.0, n=2)
assert 4.0 == s.myPow(x=-2.0, n=2)
#assert 9.26100 == s.myPow(x=2.10000, n=3)
s.myPow(x=2.10000, n=3)
#assert 1/9.26100 == s.myPow(x=2.10000, n=-3)
s.myPow(x=2.10000, n=-3)
#assert -9.26100 ==
s.myPow(x=-2.10000, n=3)
#assert -(1/9.26100) ==
s.myPow(x=-2.10000, n=-3)
print(s.myPow(x=10.00, n=64) % (10**9 + 7))
