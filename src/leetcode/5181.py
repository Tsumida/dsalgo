# 2019-9-8

class Solution:
    def distanceBetweenBusStops(self, distance: list, start: int, destination: int) -> int:
        res = 0
        end = destination
        if start > end:
            start, end = end, start

        sums = sum(distance)
        # start <= end
        if start != end:
            tmp = sum(distance[start:end])
            res = min(tmp, sums - tmp)

        return res
