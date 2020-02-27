
from typing import List

# Raft, counting replicas.
def couting_replicas(matched_index: List[int], leader_index:int) -> int:
    n = len(matched_index)
    cnt = n >> 1
    new_arr = matched_index[:leader_index] + matched_index[leader_index+1:]
    new_arr.sort(reverse=True)
    print("cnt=", cnt, new_arr)
    return new_arr[cnt-1]

assert 1 == couting_replicas([0, 0, 0, 1, 1], 0)
assert 17 == couting_replicas([0, 0, 0, 17, 28], 2)
assert 67 == couting_replicas([0, 0, 0, 67, 67], 2)
assert 3 == couting_replicas([1, 2, 3, 0, 5], 3)
assert 1 == couting_replicas([1, 1, 1], 0)
assert 3 == couting_replicas([10, 1, 2, 3, 4], 0) # leader.commitIndex must <= others.
assert 100 == couting_replicas([100] * 10, 0)
