
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # a b
        # c d  ==> a<b, a<c, b<d, c<d
        def method_1(mat:List[List[int]], tar:int) -> bool:
            # O(n+m)
            # 一个观点，把右上角作为根，有点像BST
            n = len(mat)
            if n == 0:
                return False
            m = len(mat[0])
            if m == 0:
                return False
            i, j = 0, m-1
            path = ""
            res = False
            while i >= 0 and i < n and j >= 0 and j < m:
                num = mat[i][j]
                path += f"->{num}"
                if tar == num:
                    res = True
                    break
                elif tar < num:
                    j -= 1
                else:
                    i += 1
            print(path)
            return res

        res = method_1(matrix, target)
        print(res)
        return res


s = Solution()
mat1 = [
  [1,   4,  7, 11, 15], # 一个观点，把右上角作为根，有点像BST
  [2,   5,  8, 12, 19], # target=5, 15 -> 11 -> 7 -> 4 -> 5
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30],
]

assert True == s.findNumberIn2DArray(matrix=mat1, target=5)
assert False == s.findNumberIn2DArray(matrix=mat1, target=100)
assert True == s.findNumberIn2DArray(matrix=mat1, target=15) # 右上
assert True == s.findNumberIn2DArray(matrix=mat1, target=1)  # 左上
assert True == s.findNumberIn2DArray(matrix=mat1, target=18) # 左下
assert True == s.findNumberIn2DArray(matrix=mat1, target=30) # 右下
assert True == s.findNumberIn2DArray(matrix=mat1, target=16)
