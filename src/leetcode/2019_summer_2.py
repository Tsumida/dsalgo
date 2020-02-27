def gcd(n, m):
    """
    1. gcd(n, m) = gcd(n, n % m)
    2. gcd(n, n) = gcd(n, 0) = |n|
    3. gcd(n, 1) = 1
    4. for all 0 < y <= x, x % y <= x/2
    5. gcd(a, b) = gcd(b, a) = gcd(-a, b) = gcd(|a|, |b|)

    :param a:
    :param b:
    :return gcd(a, b):
    """
    n, m = abs(n), abs(m)
    if n < m:
        n, m = m, n
    while m > 0:
        temp = n
        n = m
        m = temp % m
    return n

class Solution:
    def fraction(self, cont: list) -> list:
        # 化简连分数
        a, b = cont[-1], 1  # a / b
        n = len(cont)

        index = n-2
        while index >= 0:
            a, b = cont[index] * a + b, a
            gcd_fac = gcd(a, b)
            a, b = a // gcd_fac, b // gcd_fac
            index -= 1

        return [a, b]

s = Solution()
assert [13, 4] == s.fraction(cont = [3, 2, 0, 2])
assert [3, 1] == s.fraction(cont = [0, 0, 3])
