def quick_sort(arr: list, reverse=False):
    def inner_sort(left: int, right: int, rev=False):
        if left+1 < right:
            pivot = partition(arr, left, right, rev)
            inner_sort(left, pivot, rev)
            inner_sort(pivot+1, right, rev)

    n = len(arr)
    if n <= 1:
        return
    inner_sort(0, n, reverse)


def partition(arr: list, left: int, right: int, reverse=False) -> int:
    pivot = arr[left]
    p, q = left, right-1
    # 考虑 reverse = False
    # 这个算法只适合 pivot_index = left的情况
    # 最初, arr[p] <= pivot成立
    # 此过程每一次循环都保证了 pivot == arr[p]
    while p < q:
        # 归纳法: 假设每次循环arr[p] == pivot
        # 从右往左找到第一个 <= pivot 的元素
        while p < q and ((arr[q] > pivot) ^ reverse):
            q -= 1
        if p < q:
            # 此时 arr[q] <= pivot，故将arr[p]与arr[q]交换，arr[q]==pivot
            tmp = arr[p]
            arr[p] = arr[q]
            arr[q] = tmp
            p += 1
        # 从左往右找第一个 >= pivot 的元素
        while p < q and ((arr[p] < pivot) ^ reverse):
            p += 1
        if p < q:
            # 交换，于是pivot又回到了arr[p]上
            tmp = arr[p]
            arr[p] = arr[q]
            arr[q] = tmp
            q -= 1
    #print(left, right, arr, "p = ", p)
    return p


def test_partition():
    case = [5, 3, 2, 7, 9, 6]
    partition(case, 0, 6)
    assert 2 == case.index(5)

    case2 = [5] * 5
    partition(case2, 0, 5)
    assert case2.index(5) in [0, 1, 2, 3, 4]

    case3 = [100, 7, 6, 7, 8, 9, 3]
    partition(case3, 0, 7)
    assert case3.index(100) == 6

    case = [5, 3, 2, 7, 9, 6]
    partition(case, 0, 6, True)
    assert 3 == case.index(5)

    case2 = [5] * 5
    partition(case2, 0, 5, True)
    assert case2.index(5) in [0, 1, 2, 3, 4]

    case3 = [100, 7, 6, 7, 8, 9, 3]
    partition(case3, 0, 7, True)
    assert case3.index(100) == 0


test_partition()












