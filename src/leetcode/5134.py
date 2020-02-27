# 2019-12-28

class Solution:
    def replaceElements(self, arr:list) -> list:
        if len(arr) > 0:
            tmp: int = arr[-1]
            arr[-1] = -1
            n = len(arr)
            for i in range(n-2, -1, -1):
                tmp2 = arr[i]
                # a(i) = max( a'(i+1), a(i+1))
                arr[i] = max(arr[i+1], tmp)
                tmp = tmp2
                #print(arr)

        return arr

s = Solution()
assert [18,6,6,6,1,-1] == s.replaceElements(arr = [17,18,5,4,6,1])
assert [] == s.replaceElements(arr = [])
assert [1, 1, 1, -1] == s.replaceElements(arr = [1, 1, 1, 1])
assert [3, 3, 3, -1] == s.replaceElements(arr = [1, 2, 3, 3])
