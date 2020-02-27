
# 2019-5-1

import math
import sys
sys.path.append("..\..")

import testFunctions as tfs

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        vec_sqr = list()

        for num in range(1, n+1):
            #print(math.sqrt(num))
            sqr =  int((math.sqrt(num))) ** 2
            delta = 0
            if sqr == num:
                dp[num] = 1
                vec_sqr.append(num)
            else:
                temp = 1 << 20
                for ps_num in vec_sqr:
                    delta = num - ps_num
                    temp = min(temp, dp[delta] + 1)
                dp[num] = temp
            #print(" == ", num, sqr, delta)

        return dp[n]

    @tfs.timer
    def test(self):
        test_cases = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 1),
            (5, 2),
            (6, 3),
            (7, 4),
            (12, 3),
            (13, 2),
            (17, 2),
            (19, 3),
            (6337, 2),
            (10000, 1),
            (40000, 1),
            (40017, 3),
            #(10019, 4),
        ]



        tfs.test(self.numSquares, test_cases)

Solution().test()
