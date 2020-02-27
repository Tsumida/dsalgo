# 2019-9-13
import sys
sys.path.append("..")


def is_palindrome(string: str):
    if not string:
        return False
    else:
        res = True
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                res = False
                break
            left, right = left + 1, right - 1
        return res

def test_is_palindrome():
    test_cases = [
        (False, ""),
        (True, "a"),
        (True, "aaa"),
        (False, "abc"),
        (True, "abaaba"),

    ]

    for x in test_cases:
        a, i = x
        o = is_palindrome(i)
        print(o, a)
        assert o == a



class Solution:
    # len(s) <= 1000
    # 超时
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        # 递推方程: dp[0, n] = dp[0, n-1] + count( true == is_palindrome(f[i, n]) for i in [0, n]), O(n^2)
        for end in range(1, n+1):
            res += sum(1 for i in range(0, end+1) if is_palindrome(s[i:end]) )

        return res

    # 比上面更快
    def spanning_way(self, s:str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            # 利用了回文子串的一个性质:
            # ps[a, b] 是回文 --> ps[a-1, b-1]也是
            start, end = i, i
            while start >= 0 and end < n and s[start] == s[end]:
                res += 1
                start -= 1
                end += 1
            start, end = i, i+1 # 偶数回文
            while start >= 0 and end < n and s[start] == s[end]:
                res += 1
                start -= 1
                end += 1



        return res

test_is_palindrome()

s = Solution()
test_cases = [
    (0, ""),
    (6, "aaa"), # a, a, a, aa, aa, aaa
    (3, "abc"), # a, b, c
    (4, "aba"), # a, b, a, aba
    (6, "aaba"),
    (6, "abaa"),
    (55, "a"*10),
    (1000*(1001)//2, "a"*1000),
]
'''
for i, case in enumerate(test_cases):
    ans, inp = case
    out = s.countSubstrings(s=inp)
    assert ans == out, "\ncase {} failed. for ans = {}, out = {}\nargs = {}".format(
        i, ans, out, case
    )
'''
for i, case in enumerate(test_cases):
    ans, inp = case
    out = s.spanning_way(s=inp)
    assert ans == out, "\ncase {} failed. for ans = {}, out = {}\nargs = {}".format(
        i, ans, out, case
    )
