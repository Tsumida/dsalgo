# 2019-9-7

class Solution:
    def countLetters(self, S: str) -> int:
        if len(S) < 2:
            return len(S)
        else:
            prev_sum = 0
            # split aaaba --> aaa b a
            start, end = 0, 1
            n = len(S)
            while start < n and end <= n:

                while end < n and S[start] == S[end]:
                    end += 1
                # [start, end) 是 同字符的子串
                lens = (end - start)
                prev_sum += ((lens+1) * lens ) // 2

                start = end
                end = start + 1

                #print("S = ", S, prev_sum)

            return prev_sum


s = Solution()
assert 1 == s.countLetters(S="a")
assert 3 == s.countLetters(S="aa")
assert 6 == s.countLetters(S="aaa")
assert 10 == s.countLetters(S="aaaa")
assert 7 == s.countLetters(S="aaab")
assert 8 == s.countLetters(S="aaaba")
assert 4 == s.countLetters(S="abcd")
assert 14 == s.countLetters(S="aaababbb")
