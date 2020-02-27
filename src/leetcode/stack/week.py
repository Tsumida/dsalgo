# 2019-9-1


class Solution:
    def dietPlanPerformance(self, calories: list, k: int, lower: int, upper: int) -> int:
        res = 0
        start = 0
        n = len(calories)
        while start < n:
            sums = sum(calories[start:start+k])
            if sums < lower:
                res -= 1

            if sums > upper:
                res += 1

            start += k


        return res

s = Solution()

assert 0 == s.dietPlanPerformance(calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3)
assert 1 == s.dietPlanPerformance(calories = [3,2], k = 2, lower = 0, upper = 1)
assert 0 == s.dietPlanPerformance(calories = [6,5,0,0], k = 2, lower = 1, upper = 5)
assert 3 == s.dietPlanPerformance(calories = [6,13,8,7,10,1,12,11], k = 6, lower = 5, upper = 37) # Why 3 ?

