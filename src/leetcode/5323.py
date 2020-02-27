# 2020-
from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def cmp(num:int) -> int:
            cnt = 0
            while num > 0:
                if num & 1 == 1:
                    cnt += 1
                num = num >> 1
            return cnt


        arr.sort(key=lambda x: (cmp(x), x))
        print(arr)
        return arr

s = Solution()
assert s.sortByBits(arr=[1, 2, 4]) == [1, 2, 4]
assert s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7]
assert s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]) == [1,2,4,8,16,32,64,128,256,512,1024]
assert s.sortByBits(arr = [10000,10000]) == [10000,10000]
assert s.sortByBits(arr = [2,3,5,7,11,13,17,19]) == [2,3,5,17,7, 11,13,19]
