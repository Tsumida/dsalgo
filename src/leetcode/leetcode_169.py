# 2018-12-16

# leetcode 169, divide and conquer

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 先排序，再选..

        # case 1 : 众数a 横跨 sub1 与 sub2
        # case 2： a 再 sub1
        # case 3： a 再 sub2

        # O(nlgn)
        arr = sorted(nums)
        last = len(arr) - 1
        mid = last // 2

        if len(arr) == 0:
            return None
        elif len(arr) == 1:
            return arr[0]


        if arr[mid] == arr[mid+1]:
            return arr[mid]
        else:
            res = -1
            max_len = 0
            lens = len(arr)
            sub_len = 0
            index = 0
            # O(n)
            while index < lens-1:
                if arr[index] != arr[index+1]:
                    if max_len < sub_len:
                        res = arr[index]
                        max_len = sub_len
                    sub_len = 0
                else:
                    sub_len += 1
                index += 1
        return res

    def test(self):
        case_1 = [3, 2, 3]                      # 3
        case_2 = [2, 2, 1, 2, 1, 1, 1, 2, 2]    # 2
        case_3 = [1, 2, 2, 2, 3, 3, 4]          # 2
        case_4 = [1, 1, 1, 1, 2, 2, 2]          # 1
        case_5 = [2, 2, 2, 2, 3, 1, 5, 1, 9]    # 2
        case_6 = [1]                            # 1
        case_7 = [2, 2]                         # 1

        print(self.majorityElement(case_1))
        print(self.majorityElement(case_2))
        print(self.majorityElement(case_3))
        print(self.majorityElement(case_4))
        print(self.majorityElement(case_5))
        print(self.majorityElement(case_6))
        print(self.majorityElement(case_7))

# fastest code.
class Solution_2:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] +=1
        return max(dict1,key=dict1.get)



s1 = Solution()
s1.test()
