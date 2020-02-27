# 2019-10-27

class Solution:
    def circularPermutation(self, n: int, start: int) -> list:
        rest = []
        # 对称法
        m = 2 ** n
        table = [[0 for i in range(n)] for j in range(m)]
        table[1][-1] = 1
        x = 1 #
        while x < n:
            '''     low     high  
                      | x-1 |
                    ---------
                    | |     |
                    | |     |
                    ------------- roller
                    | |     |   i
                    | |     |   ↓
                    ---------
                      ←--- j
            '''
            roller = 1 << x
            for j in range(n-1, n-x-1, -1):
                for i in range(roller, roller << 1):
                    table[i][j] = table[2 * roller - i - 1][j]

            for i in range(roller, roller << 1):
                table[i][n-x-1] = 1

            x += 1

        for row in table:
            print(row)

        # list[int] to int
        for line in table:
            rest.append(sum( (2 ** i) * bit for i, bit in enumerate(line)))
        print(rest)

        # find start. swap (start + i ) % n with start % n
        start_index = rest.index(start)
        res = rest[start_index:] + rest[0: start_index]

        print(res)
        return res

s = Solution()
_ = s.circularPermutation(n=6, start=2)
