
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        res = []
        t1, t2 = dict(), dict()
        for x in nums1:
            if x in t1:
                t1[x] += 1
            else:
                t1[x] = 1
        for x in nums2:
            if x in t2:
                t2[x] += 1
            else:
                t2[x] = 1

        for k, v in t1.items():
            p = t2.get(k, 0)
            if p > 0:
                res.extend([k] * min(v, p))
        #print(t1)
        #print(t2)
        #print(res)

        return res

s = Solution()
print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2])) # [2, 2]
print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])) # [4, 9]
print(s.intersect(nums1 = [4,9,5], nums2 = [6, 6, 6])) # []
print(s.intersect(nums1 = [4,9,5], nums2 = [4, 9, 5])) # []
print(s.intersect(nums1 = [4,9,5, 5], nums2 = [4, 4, 4, 5])) # []
