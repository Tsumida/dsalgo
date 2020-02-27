# 2019-4-30
import sys
sys.path.append("..\..")

import testFunctions as tfs

class Solution:
    def minFallingPathSum(self, A:list) -> int:

        res = 0

        mat = [[0 for x in range(len(A))],
               A[0].copy()]
        row, col = len(A), len(A[0])
        for level in range(1, row):

            prev_s, present_s = 0, 1
            mat[prev_s] = mat[present_s].copy()

            #mat[present_s] = [0 for i in range(col)]
            for i, ele in enumerate(mat[present_s]):
                """
                    1 2 3 4 5 6 7 8 9
                    
                    1 2 3 4 5 6 7 8 9
                    
                    State transfer equation:
                    for level = L:
                        if i == 0:
                            present[i] = min(prev_s[i], prev_s[i+1]) + A[L][i]
                        else if i < col-1
                            present[i] = min(prev_s[i-1],
                                             prev_s[i], 
                                             prev_s[i+1]) + A[L][i]
                        else i == col-1
                            present[i] = min(prev_s[i-1], prev_s[i]) + A[L][i]
                
                
                """
                if i == 0:
                    mat[present_s][i] = min(mat[prev_s][i],
                                         mat[prev_s][i+1])
                elif i < col-1:
                    mat[present_s][i] = min(
                                        mat[prev_s][i-1],
                                        mat[prev_s][i],
                                        mat[prev_s][i+1])
                else:
                    mat[present_s][i] = min(
                                        mat[prev_s][i-1],
                                        mat[prev_s][i])
                mat[present_s][i] += A[level][i]
            #print(mat[present_s])

        res = min(mat[1])

        return res

    @tfs.timer
    def test(self):
        test_cases = \
            [
                ([[1,2,3],
                  [4,5,6],
                  [7,8,9]], 12),
                ([[2, 3, 4], # 2, 3, 4
                 [5, 7, 2], # 7, 9, 5
                 [3, -2, 1]], 3), # 10, 3, 6,
                ([[1] * 3000] * 3000, 1000)
            ]

        #@tfs.timer
        tfs.test(self.minFallingPathSum, test_cases)


s = Solution()
s.test()
