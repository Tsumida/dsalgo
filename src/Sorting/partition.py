from typing import List
from unittest import TestCase
from random import randint

# Partition通用框架, 将nums分为两半，前一半的元素满足pred, 后一半不满足pred.
# pred是一个谓词
def partition(nums: List[int], pred) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums

        p, q = 0, n-1
        while p < q:
            while p < q and pred(nums[p]):
                p += 1
            while p < q and not pred(nums[q]):
                q -= 1
            # 因为要交换p,q所以上面两个元素
            if p < q:
                tmp = nums[p]
                nums[p] = nums[q]
                nums[q] = tmp
            # assert pred(nums[p]) and not pred(nums[q])
        return nums

SIZE = 15
CASES = [
    ("01", lambda x: x == 0, [randint(0, 1) for _ in range(SIZE)]),
    (">1000, <=1000",
     lambda x: x > 1000,
     [randint(0, 999) for _ in range(SIZE>>1)] + [1000] +
     [randint(1001, 1999) for _ in range(SIZE>>1)])
]

class TestPartition(TestCase):

    def test_01(self):
        label, pred, lis = CASES[0]
        print("test " + label)
        ans = lis.copy()
        ans.sort()
        partition(lis, pred=pred)
        assert lis == ans, "Error, \nlis={}\nans={}".format(lis, ans)

    def test_1000(self):
        label, pred, lis = CASES[1]
        print("test " + label)
        partition(lis, pred=pred)
        index = lis.index(1000)
        assert index != -1
        assert all(pred(x) for x in lis[:index])
        assert all(not pred(x) for x in lis[index+1:])
