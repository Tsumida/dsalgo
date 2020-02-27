# 2020-02-24

from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # nums长度为n, 所有输入都在[0, n)之间
        def method_1(arr:List[int]) -> int:
            # HashMap-based. O(n)
            hmap = set()
            for ele in arr:
                if ele not in hmap:
                    hmap.add(ele)
                else:
                    return ele # 返回任意一个
            raise Exception("Error, no repetition.")

        def method_2(arr:List[int]) -> int:
            # 利用了数字分布在[0, n)的特点
            # 如果数字num不重复，那么它只能放在index=num的桶中
            # 也就是说，如果index=num的桶上面的数字是num, 而此时还有一个num，那就输出。
            for i, ele in enumerate(arr):
                 if ele != i:
                    if ele == arr[ele]: # repetition
                        return ele
                    num = arr[ele]
                    arr[ele] = ele
                    arr[i] = num

            raise Exception("Error, no repetition.")

        if len(nums) < 2:
            raise Exception("Error")
        res = method_2(nums)
        print(res)
        return res



s = Solution()
assert s.findRepeatNumber(nums=[2, 3, 1, 0, 2, 5, 3]) in [3, 2]
assert 2 == s.findRepeatNumber(nums=[2] * 10)
assert s.findRepeatNumber(nums=[1, 2, 3, 3, 1, 2]) in [1, 2, 3]

