# 2020-01-09
from typing import List
from cProfile import Profile



class Solution:
    # timeout for [0] * 10000
    # see https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = set()
        hmap = dict()
        for i, a in enumerate(nums):
            hmap.setdefault(a, list()).append(i)

        for j, b in enumerate(nums):
            for k, c in enumerate(nums[j+1:]):
                lis = hmap.get(-(b+c), list())
                for i in lis:
                    # 注意nums[j+1:] 中的nums[0] 对应完整nums的 j+1+0
                    if i != j and i != k+j+1:
                        tmp = [nums[i], b, c]
                        tmp.sort()
                        res.add(tuple(tmp))


        return [list(t) for t in res]

s = Solution()
print(s.threeSum(nums=[0, 0]))
print(s.threeSum(nums=[1,2,-2,-1]))

p = Profile()
p.runcall(s.threeSum, nums=[0]*200)
p.print_stats()

