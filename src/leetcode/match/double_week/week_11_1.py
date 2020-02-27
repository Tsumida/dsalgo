
class Solution:
    def missingNumber(self, arr: list) -> int:
        res = 0
        n = len(arr) # >= 3
        arr.sort()
        delta = [arr[i] - arr[i-1] for i in range(1, n)]
        min_d = min(delta)
        candidate_index = -1
        for i, d in enumerate(delta):
            if d > min_d:
                candidate_index = i
                break
        if candidate_index != -1:
            res = min_d + arr[candidate_index]

        return res

s = Solution()
assert 9 == s.missingNumber(arr=[1, 3, 5, 7, 11])
assert 2 == s.missingNumber(arr=[0, 1, 3, 4])
assert 14 == s.missingNumber(arr=[15, 13, 12])
assert -1 == s.missingNumber(arr=[-3, -2, 0])
