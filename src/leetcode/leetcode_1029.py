
# 2019-5-18

class Solution:
    def twoCitySchedCost(self, costs: list) -> int:

        res = 0
        dp = list()
        N = len(costs) // 2
        # Consider B-A rather than costA, costB
        cost_delta = [((b-a), i) for i, (a, b) in enumerate(costs)]
        cost_delta.sort(key=lambda delta: delta[0])

        # first N people go to city B
        for _, i in cost_delta[:N]:
            res += costs[i][1]
        for _, i in cost_delta[N:]:
            res += costs[i][0]
            
        print(res)    
    
        return res
