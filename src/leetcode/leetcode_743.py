# 2018-11-28

# leetcode_743

from queue import *

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        res = -1
        INF = 1 << 29
        dist = [INF for i in range(N+1)]
        dist[K] = 0

        # build adj_list
        # do not use this --- causes a[i] != a[j] refer to the same list.
        adj_list = [[] for i in range(N+1)]
        for it in times:
            adj_list[it[0]].append((it[1], it[2]))

        for x in adj_list:
            print(x)


        # put into Q
        Q = PriorityQueue()
        Q.put((K, dist[K]))
        while not Q.empty():
            node = Q.get()
            u, dist_u = node
            # (u, v) and w = weight(u, v)
            for v, w in adj_list[u]:
                newLen = dist_u + w
                print("----({}, {}) newLen: {}\t : ".format(u, v, newLen))
                if newLen < dist[v]:
                    dist[v] = newLen
                    Q.put((v, newLen))
                for x in dist:
                    print(x, end=' ')
                print('\n')


        # find max
        res = max(dist[1: N+1])
        if res == INF:
            res = -1

        return res



def main():
    test = ([
        [2,1,1],
        [2,3,1],
        [3,4,1]
    ], 4, 2)

    test2 = ([[1,2,1]], 2, 2)


    test3 = ([[1,2,1],[2,3,2],[1,3,1]], 3, 2)
    test4 = ([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
    s = Solution()
    print(s.networkDelayTime(test[0], test[1], test[2]))
    print(s.networkDelayTime(test2[0], test2[1], test2[2]))
    print(s.networkDelayTime(test3[0], test3[1], test3[2]))
    print(s.networkDelayTime(test4[0], test4[1], test4[2]))

if __name__ == "__main__":
    main()
