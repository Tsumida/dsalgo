
def merge_sort(arr:list, reverse=False):
    def inner_sort(left: int, right: int, rev=False):
        if left+1 < right:
            mid = (left + right) >> 1
            inner_sort(left, mid)
            inner_sort(mid, right)
            merge(tmp_list, arr, left, mid, right, reverse)

    n = len(arr)
    if n == 0:
        return
    tmp_list = arr.copy()
    inner_sort(0, n, reverse)

def merge(tmp_list: list, target: list, left: int, mid:int, right: int, reverse=False):
    """
    Given two sorted array [left, mid), [mid+1, right),
    sort target[left, right)
    """
    if left >= mid or mid >= right:
        return
    p, q, k = left, mid, left
    while p < mid and q < right:
        flag = (target[p] <= target[q]) ^ reverse
        if flag:
            tmp_list[k] = target[p]
            p+=1
        else:
            tmp_list[k] = target[q]
            q+=1
        k += 1

    st, end = p, mid
    if q < right:
        st, end = q, right

    for i in range(st, end):
        tmp_list[k] = target[i]
        k+=1

    for i in range(left, right):
        target[i] = tmp_list[i] # cover target[left, right)
    #print("l, r = ", left, right, "-"*(left+1), target[left:right])


def test_merge():
    case1 = [1, 4, 6, 2, 3, 5]
    tmp1 = [0] * 6
    merge(tmp1, case1, 0, 3, 6)
    assert case1 == [1, 2, 3, 4, 5, 6]

    case1 = [1, 2]
    tmp1 = [0] * 2
    merge(tmp1, case1, 0, 1, 1)
    assert case1 == [1, 2]

    case1 = [1, 7, 9, 13, 2, 3, 4]
    tmp1 = [0] * 7
    merge(tmp1, case1, 0, 4, 7)
    assert case1 == [1, 2, 3, 4, 7, 9, 13]

    case1 = [1, 7, 9, 2, 3, 4, 13]
    tmp1 = [0] * 7
    merge(tmp1, case1, 0, 3, 7)
    assert case1 == [1, 2, 3, 4, 7, 9, 13]

test_merge()
