# 2019-2-26

# search matrix

'''
input : matrix with elements that:
            a  <=  b
            <=    <=
            c  <=  d
'''

class Solution:

    def binary_search(self, row: list, target: int) -> bool:
        res = False
        left, right = 0, len(row)-1
        while left <= right:
            mid = (right + left) // 2
            if row[mid] == target:
                res = True
                break
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return res

    def searchMatrix(self, matrix, target) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool


        """
        res = False
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False

        # O(m)
        for row in matrix:
            if row[0] <= target:
                res = self.binary_search(row, target) # O(logn)
            if res == True:
                break
        return res

    def test_bs(self):
        test_matrix_1 = [1, 4, 7, 11, 15, 19, 30, 100]


        search_case = [1, 4, 7, 12, 14, 30, 99, 100]

        for ele in search_case:
            print(self.binary_search(test_matrix_1, ele))



    def test(self):
        test_matrix_1 = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]

        test_case_1 = [
            (1, True), (7, True), (3, True), (9, True), (18, True), (19, True), (30, True), (24, True),
            (35, False), (27, False), (-1, False)
        ]

        for i, e in enumerate(test_case_1):
            *inp, ans = e
            oup = self.searchMatrix(test_matrix_1, *inp)
            assert ans == oup, "test-{} failed.\nleft = {}, right = {} for parameter:\n{}".format(
                i, ans, oup, inp
            )

s1 = Solution()
s1.test()
#s1.test_bs()
