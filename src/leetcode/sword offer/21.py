from typing import List
from random import randint
class Solution:
    # partition.
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums

        p, q = 0, n-1
        while p < q:
            # p < q and [0, p)都是奇数
            # p指向偶数， q指向一个奇数
            while p < q and nums[p] % 2 == 1:
                p += 1

            while p < q and nums[q] % 2 == 0:
                q -= 1
            if p < q:
                tmp = nums[p]
                nums[p] = nums[q]
                nums[q] = tmp
        print(p, q, nums)

        return nums

s = Solution()
s.exchange(nums=[1, 3, 5, 7, 9])
s.exchange(nums=[2, 4, 6])
s.exchange(nums=[1, 2, 3, 4, 5])
s.exchange(nums=[randint(0, 100) for _ in range(16)])
