# 2019-5-19

import queue

class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        res = 0
        pq = queue.PriorityQueue()

        for stone in stones:
            pq.put( -1 * stone)

        while pq.qsize() > 1:
            o1, o2 = pq.get(), pq.get()
            y, x = min(o1, o2), max(o1, o2) # a < b => -b < -a
            if x != y:
                pq.put(y-x)

        if pq.qsize() == 1:
            res = -1 * pq.get()

        return res
