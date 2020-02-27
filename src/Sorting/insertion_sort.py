def insertion_sort(arr:list, reverse=False):
    n = len(arr)
    if n <= 1:
        return
    if reverse:
        for i in range(1, n):
            # assume [0, i) is sorted
            index = -1
            ele = arr[i]
            for j in range(0, i):
                if ele > arr[j]:
                    index = j
                    break
            if index != -1:
                move(arr, index, i)
                arr[index] = ele
    else:
        for i in range(1, n):
            index = -1
            ele = arr[i]
            for j in range(0, i):
                if ele < arr[j]: # all in [0, j) <= ele
                    index = j
                    break
            if index != -1:
                move(arr, index, i)
                arr[index] = ele



# [start, end) --> (start, end]
def move(arr:list, start:int, end:int):
    assert start >= 0 and end < len(arr)
    tmp = arr[end]
    for i in range(end, start, -1):
        arr[i] = arr[i-1]
    return tmp


def test_move():
    case1 = [0, 1, 2, 3, 4, 5]
    st, end = 1, 4 # [1, 4)
    assert 4 == move(case1, st, end)
    assert case1 == [0, 1, 1, 2, 3, 5]

    case2 = [0, 1, 2, 8, 9, 5]
    st, end = 3, 5
    assert 5 == move(case2, st, end)
    case2[st] = 5
    assert case2 == [0, 1, 2, 5, 8, 9]

    case2 = [0, 1]
    st, end = 0, 1
    assert 1 == move(case2, st, end)
    assert case2 == [0, 0]
