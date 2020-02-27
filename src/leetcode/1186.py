# 2019-9-9
def max_sum_sub_seq(arr: list):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        n = len(arr)
        dp = [0 for _ in range(n)]
        # dp[n] 所有以 arr[n]结尾的子串中最大连续和
        # dp[n] = max(dp[n-1] + arr[n],  arr[n]), 因为必须包含arr[n], 那么只有两种可能： arr[0, n]或者arr[n, n]
        dp[0] = arr[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + arr[i], arr[i])

        # print(dp)
        return max(dp)  # 子串不可以为空


def test_msss():
    c1 = [1]                 # 1
    c2 = [-1, -2, -3]        # -1    #
    c3 = [1, 2, 3, 4, 5]     # 15
    c4 = [1, 2, 3, -4, 5]    # 7
    c5 = [-1, -2, -3, 4, 5]  # 9
    c6 = [1, 2, 3, -4, -5]   # 6

    assert 0 == max_sum_sub_seq(arr=[])
    assert 1 == max_sum_sub_seq(arr=c1)
    assert -1 == max_sum_sub_seq(arr=c2)
    assert 15 == max_sum_sub_seq(arr=c3)
    assert 7 == max_sum_sub_seq(arr=c4)
    assert 9 == max_sum_sub_seq(arr=c5)
    assert 6 == max_sum_sub_seq(arr=c6)


class Solution:

    def maximumSum(self, arr: list) -> int:

        n = len(arr)
        assert n > 0

        if n == 1:
            return arr[0]
        else:
            no_del = [0 for _ in range(n)]
            del_one = no_del.copy()
            no_del[0] = arr[0]

            # del_one[1] = max(del_one[0] + arr[1], no_del[0])
            # 因为子串至少一个元素， 所以有:
            # del_one[0] < no_del[0] - arr[1] = arr[0] - arr[1], 后者最小为 -20000
            del_one[0] = -200001

            for i in range(1, n):
                # 最大为[0, .., i]， 或为 arr[i, i]
                no_del[i] = max(no_del[i-1] + arr[i], 0 + arr[i])
            for i in range(1, n):
                # 使用了一次del分两种情况
                # 1. 之前使用了， arr[i]不能用
                # 2. 之前没有， 删去arr[i]
                del_one[i] = max(del_one[i-1] + arr[i], no_del[i-1] + 0)
            print("--", arr)
            print(no_del)
            print(del_one)
            return max(max(no_del), max(del_one))


def test_maximumSum():
    s = Solution()

    assert 7 == s.maximumSum(arr=[1,-4,-5,-2,5,0,-1,2])
    assert -50 == s.maximumSum(arr=[-50])
    assert 14 == s.maximumSum(arr=[-7, 6, 1, 2, 1, 4, -1])
    assert 3000 == s.maximumSum(arr=[1]*3000)
    assert 3 == s.maximumSum(arr=[1, 1, 1, -2, -3, 1, 1])
    assert 8 == s.maximumSum(arr=[1, -2, 3, -4, 5])
    assert 1 == s.maximumSum(arr=[1])
    assert 4 == s.maximumSum(arr=[1,-2,0,3])
    assert 3 == s.maximumSum(arr=[1,-2,-2,3])
    assert -1 == s.maximumSum(arr=[-1,-1,-1,-1])


test_msss()
# test_n3_solution()
test_maximumSum()
