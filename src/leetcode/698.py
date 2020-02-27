# 2019-8-16

import time

"""
# 一种基于贪心策略的改进方法
 def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < k:  # 为空或不够分
            return False
        avg, mod = divmod(sum(nums), k)
        if mod:  # 不能整除
            return False
        nums.sort(reverse=True)  # 倒序排列
        if nums[0] > avg:  # 有超过目标的元素
            return False
        used = set()  # 记录已使用的数

        def dfs(k, start=0, tmpSum = 0):  # 当前还需要凑的avg个数，当前从哪个数开始考虑，以及当前已凑够的和
            if tmpSum == avg:  # 如果已凑满一个
                return dfs(k-1, 0, 0)  # 那么从最大数重新开始考虑，凑下一个
            if k == 1:  # 只剩最后一个，那么剩下的没使用的数加起来肯定凑满
                return True
            for i in range(start, len(nums)):  # 优先用大的数的凑
                if i not in used and nums[i]+tmpSum <= avg:  # 如果该数未使用并且可以用来凑
                    used.add(i)  # 使用该数
                    if dfs(k, i+1, nums[i]+tmpSum):  # 继续用比该数小的数来凑
                        return True
                    used.remove(i)  # 没有得到可用方案，则换个数来凑
            return False

        return dfs(k)

作者：mai-mai-mai-mai-zi
链接：https://leetcode-cn.com/problems/two-sum/solution/pythonzhi-guan-de-zan-shu-si-lu-hui-su-fa-jia-jian/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


"""

def timer(func):

    def real_timer(*args, **kwargs):
        s0 = time.time()
        res = func(*args, **kwargs)
        s1 = time.time() - s0
        print("time cost: {:.8f} s\tresult = ".format(s1, res))
    return real_timer

class Solution:
    @timer
    def canPartitionKSubsets(self, nums: list, k: int) -> bool:
        '''
        不够快， t7耗时17s
        :param nums:
        :param k:
        :return:
        '''
        def recur(index:int ) -> bool:

            if index < len(nums):
                for x in range(k):
                    assign[x] += nums[index]
                    # 预先计算一次， 节省is_valid
                    # t7 cnt 从 4000w 降到 900w
                    if assign[x] <= p :
                        if index == len(nums) - 1 and all(s == p for s in assign):
                            return True
                        elif recur(index + 1):
                            return True
                    assign[x] -= nums[index]

                return False
            else: # index 异常
                return False

        res = False
        p = sum(nums) // k
        assign = [0 for x in range(k)]
        if p * k == sum(nums):
            res = recur(0) # 从第一个进行

        self.cnt_judge = 0
        return res

s = Solution()

print("t1 = ", s.canPartitionKSubsets(nums = [4, 3, 2, 3, 5, 2, 1], k = 4))
print("t2 = ", s.canPartitionKSubsets(nums = [1, 1, 1, 1], k = 4))
print("t3 = ", s.canPartitionKSubsets(nums = [0, 0, 0, 1], k = 4))
print("t4 = ", s.canPartitionKSubsets(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k = 5))
print("t5 = ", s.canPartitionKSubsets(nums = [10,10,7,7,7,7,6,6], k = 2))
print("t6 = ", s.canPartitionKSubsets(nums = [10,10,10,7,7,7,7,7,7,6,6,6], k = 3))
print("t7 = ", s.canPartitionKSubsets(nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], k = 5))
