from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # for [a0, a1, .., an-1] -> rotate -> [ai, ai+1, .., a0, a1, .., ak]
        # return a0
        def method_1(arr: List[int]) -> int:
            # O(n)
            n = len(arr)
            if n == 1:
                return arr[0]
            for i in range(1, n):
                if arr[i-1] > arr[i]:
                    return arr[i]
            raise Exception("Error, invalid input.")

        def method_2(arr:List[int]) -> int:
            # O(lgn)
            # 考虑重复
            # 单调递增数组旋转后，分为左右两部分，左部分任何一个都比右边的都大，而且各自升序。
            # 关键是确定什么比较条件，来缩减[left, right]
            left, right = 0, len(arr)-1
            while left < right:
                # 每个循环都要保证 x in [left, right]
                mid = (left + right) >>1
                if arr[mid] == arr[right]:
                    # 无法确定mid在左边还是右边，
                    # 但是x in [left, right]成立
                    right -= 1
                elif arr[mid] > arr[right]:
                    # 显然，mid在左边; 那么 mid + 1可能在左边，也可能在右边
                    # 那么 x 必然在 [mid+1, right]
                    left = mid+1
                else:
                    # 显然, mid在右边，那么 x <= mid < right
                    # 那么 x in [left, mid]
                    right = mid

            assert left == right
            return arr[left]

        res = method_2(numbers)
        print(res)
        return res

s = Solution()
assert 1 == s.minArray(numbers=[3,4,5,1,2])
assert 1 == s.minArray(numbers=[1, 2, 3, 4, 5])
assert 0 == s.minArray(numbers=[2,2,2,0,1])
assert 1 == s.minArray(numbers=[2, 1])
assert 1 == s.minArray(numbers=[3, 1, 2])
assert 0 == s.minArray(numbers=[0])
assert 0 == s.minArray(numbers=[1, 2, 2, 2, 3, 0, 0, 0])
assert 1 == s.minArray(numbers=[1, 3, 3])
assert 1 == s.minArray(numbers=[1] * 100)
