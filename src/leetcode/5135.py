class Solution:
    # 涛哥的做法 , O(M)
    def findBestValue2(self, arr: list, target: int) -> int:
        M = 100000
        c = [0 for _ in range(M)]
        for ele in arr:
            c[ele] += 1
        f = 1 << 29
        sums = sum(arr)
        ans = M - 1
        for i in range(M-2, -1, -1):
            # 累积和
            c[i] += c[i+1]
            sums -= c[i+1]
            # 差值不断变小
            if abs(sums - target) <= f:
                f = abs(sums - target)
                ans = i

        return ans


    def findBestValue(self, arr: list, target: int) -> int:
        def turn(lis: list, value):
            result = lis.copy()
            n = len(result)
            for i in range(n):
                if result[i] > value:
                    result[i] = value

            return result

        min_ele = min(arr)
        max_ele = max(arr)
        lens = len(arr)
        if min_ele * lens >= target:
            return min_ele
        if max_ele * lens <= target:
            return max_ele

        left, right = min_ele, max_ele
        tmp_sum = -1
        while left < right:
            mid = (left + right) >> 2
            lis_tmp = turn(arr, mid)
            tmp_sum = sum(lis_tmp)

        # value in [min_ele, max_ele]
