# Fuck !

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0

        # 约束： sum(|s[i] - t[i]|) <= maxCost, for flags[i] == true.
        # 目标函数 max(sum(1 for v in flags if v == True)
        #
        n = len(s)
        assert  n == len(t)
        costs = [(abs(ord(s[i]) - ord(t[i])), i) for i in range(n)]
        costs.sort(key=lambda x: x[0])

        index = 0
        sums = 0
        if costs[index][0] > maxCost:
            return 0

        print(costs)
        while index < n:
            sums += costs[index][0]
            if sums > maxCost:
                break
            else:
                index += 1
        print("res = ", index)
        return index

s = Solution()
assert 3 == s.equalSubstring(s = "abcd", t = "bcdf", maxCost=3)
assert 1 == s.equalSubstring(s = "abcd", t = "cdef", maxCost = 3)
assert 1 == s.equalSubstring(s = "abcd", t = "acde", maxCost=0)
assert 2 == s.equalSubstring(s="krrgw", t="zjxss", maxCost=19)
