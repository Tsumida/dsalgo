
# 2019-2-9

"""

给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。

"""
INF = 2 << 20

class node:
    def __init_(self, min_cost=INF, s1_cost=0, s2_cost=0):
        self.min_cost = min_cost
        self.s1_cost = s1_cost  # j
        self.s2_cost = s2_cost  # i, cost of s1[0, j)

class Solution:

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        res = -1

        s1_len = len(s1)
        s2_len = len(s2)


        """
                s1
                s     e      a
             e  INF   s      s+a
        s2   a  INF   a+s    s
             t  INF   a+s+t  s+t 
        
        state: (s1, s2)
        move : remove the last char of s1 or s2
        
        T(n, m) = min(T(n-1, m)+val(s1[n]), T(n, m-1)+val(s2[m]))
        
        dp[i][j] = (min_cost, 
                    ord(s1[0:j]),   -- total cost of s1[0, j)
                    ord(s2[0:i]))   -- i
        """

        dp = [[0 for j in range(s1_len+1)]
                    for i in range(s2_len+1)]
        for i in range(1, s2_len+1):
            dp[i][0] = dp[i-1][0] + ord(s2[i-1])

        for j in range(1, s1_len+1):
            dp[0][j] = dp[0][j-1] + ord(s1[j-1])


        for i in range(1, s2_len+1):
            for j in range(1, s1_len+1):
                # core, mmm?
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s2[i-1]),
                        dp[i][j-1] + ord(s1[j-1]),
                    )



        res = dp[s2_len][s1_len]
        return res

    def test(self):
        case_1 = ("sea", "eat")
        print(self.minimumDeleteSum(case_1[0], case_1[1]))
        #assert self.minimumDeleteSum(case_1[0], case_1[1]) == 231

        case_2 = ("delete", "leet")
        print(self.minimumDeleteSum(case_2[0], case_2[1]))
        #assert self.minimumDeleteSum(case_2[0], case_2[1]) == 403


if __name__ == "__main__":
    s1 = Solution()
    s1.test()
