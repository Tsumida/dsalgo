
import random
from typing import List

from cProfile import Profile

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 416ms
    def constructMaximumBinaryTree2(self, nums: List[int]) -> TreeNode:
        def arr2node(nums:List[int], left:int, right:int):
            if left < right:
                p = max(nums[left:right])
                index = nums.index(p)
                r = TreeNode(p)
                r.left = arr2node(nums, left, index) if left < index else None
                r.right = arr2node(nums, index+1, right) if index + 1 < right else None
                return r
            else:
                return None

        return arr2node(nums, 0, len(nums))

    # 208ms
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        p = max(nums)
        index = nums.index(p)
        r = TreeNode(p)
        r.left = self.constructMaximumBinaryTree(nums[0:index]) if index > 0 else None
        r.right = self.constructMaximumBinaryTree(nums[index+1:]) if index + 1 < len(nums) else None
        return r

def get_arr(lens: int) -> List[int]:
    lis = [i for i in range(lens)]
    random.shuffle(lis)

    return lis


LENS = 20000

def test_1():
    lis = get_arr(lens=LENS)
    s = Solution()
    _ = s.constructMaximumBinaryTree(lis)

def test_2():
    lis = get_arr(lens=LENS)

    s = Solution()
    _ = s.constructMaximumBinaryTree2(lis)


def main():
    prof = Profile()
    prof.runcall(test_1)
    prof.print_stats()

    print("-" * 20)

    prof2 = Profile()
    prof2.runcall(test_2)
    prof2.print_stats()

main()
