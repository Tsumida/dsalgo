# 2019-10-27

'''
f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
'''

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) ->list:
        res = list() # list(list(int))
        for x in range(1, 1001):
            for y in range(1, 1001):
                tmp = customfunction(x, y)
                if tmp == z:
                    res.append([x, y])
                elif tmp > z:
                    break

        return res


s = Solution()
# assert [[1,4],[2,3],[3,2],[4,1]] == s.findSolution(function_id = 1, z = 5)
