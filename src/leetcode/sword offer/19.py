class Solution:
    # DP
    # https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/dong-tai-gui-hua-chao-xiang-xi-jie-da-you-fan-ru-j/
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] 表示 s[0, i-1]和 p[0, j-1]的匹配结果，考察s[i-1]和p[j-1]
        res = False
        n, m = len(s)+1, len(p)+1

        dp = [[False for _ in range(m)] for _ in range(n)]
        dp[0][0] = True # 空串
        # init
        for j in range(1, m):
            # 因为s长度为0, 那么如果dp包含字母和 "."那匹配结果就是False
            # 如果p[j-1] 是*, 那么可以去掉p[j-2]这个字母，表示匹配一个空串
            # case: s= "", p = "c*a*"
            # 不会出现 p以*开头的情况
            dp[0][j] = (p[j-1] == "*" and dp[0][j-2])

        for i in range(1, n):
            for j in range(1, m):
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == ".":  # 匹配任意字符
                        dp[i][j] = dp[i-1][j-1]
                    elif p[j-1] == "*":
                        # i=2,j=2   s = "cc"
                        #           p = "c*"
                        if j >= 2:
                            ch = p[j-2]
                            if ch == s[i-1] or ch == ".":
                                # 两种可能， 匹配多个字符或一个字符
                                # 前者说明 *已经匹配了至少一个, 此时s[i-2]后面再接一个相同字符，也可以匹配
                                dp[i][j] = dp[i-1][j] or dp[i][j-1]
                            # ch != s[i-1] 这时候去掉 p[j-2], 匹配一个空串
                            dp[i][j] = dp[i][j] or dp[i][j-2]
                    else:  # 两个不同的字母
                        dp[i][j] = False
        #for row in dp:
        #    print(row)
        return dp[n-1][m-1]

s = Solution()
assert False == s.isMatch(s="aa", p="a")
assert False == s.isMatch(s="ab", p="a")
assert False == s.isMatch(s="abcdef", p=".....") # 少一个
assert False == s.isMatch(s="ab", p=".*c")
assert True == s.isMatch(s="ac", p="ab*c")
assert True == s.isMatch(s="aa", p="a*")
assert True == s.isMatch(s="a", p="a*")
assert True == s.isMatch(s="abcdefghijk", p=".*")
assert True == s.isMatch(s="ab" + "a"*1024, p="a.aa*")
assert True == s.isMatch(s="abcdef", p="abcdef")
assert True== s.isMatch(s="ccaab", p="c*a*b")
assert True== s.isMatch(s="aab", p="c*a*b")
assert True== s.isMatch(s="", p=".*")


