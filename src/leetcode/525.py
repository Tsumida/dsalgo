# 2019-10-30

class Solution:
    # BF, O(n^2)
    def findMaxLength_bf(self, nums: list) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            # number of zero.
            cnt = 0
            for j in range(i+1, n+1):
                cnt += 1 if nums[j-1] == 0 else 0
                if 2 * cnt == j-i:
                    res = max(j-i, res)

        print(res)
        return res

    # 对消法
    #
    def findMaxLength(self, nums:list):
        n = len(nums)
        # cnt 的取值范围为 [-n, n]
        table = {
            0:-1, # 第一个为0
        }
        cnt = 0
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                cnt += 1
            else:
                cnt -= 1
            res = max(
                res, i - table.setdefault(cnt, i) # (table[cnt]), i]
            )
        #print(table)
        #print(res)

        return res


s = Solution()
assert 2 == s.findMaxLength(nums=[0, 1])
assert 2 == s.findMaxLength(nums=[0, 1, 1])
assert 4 == s.findMaxLength(nums=[0, 1, 1, 0])
assert 10 == s.findMaxLength(nums= [1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
assert 0 == s.findMaxLength(nums=[1, 1, 1,  1])
assert 0 == s.findMaxLength(nums=[1, 1, 1, 1]*10000)
