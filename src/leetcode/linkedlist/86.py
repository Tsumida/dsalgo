# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def from_list(arr: list) -> ListNode:
    head = ListNode(0)
    p = head
    for v in arr:
        p.next = ListNode(v)
        p = p.next

    return head.next

def to_list(head: ListNode) -> list:
    arr = list()
    p = head
    while p:
        arr.append(p.val)
        p = p.next

    return arr



class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 类似于快排的partition过程
        vals = to_list(head)
        n = len(vals)
        less = [v for v in vals if v < x]
        bigger = [v for v in vals if v >= x]
        #cnt = n - len(less) - len(bigger)
        #vals = less + [x] * cnt + bigger
        vals = less + bigger
        #print(vals)
        return from_list(vals)

s = Solution()
assert [1, 2, 2, 4, 3, 5] == to_list(s.partition(head=from_list([1, 4, 3, 2, 5, 2]), x=3))
assert [1, 3, 2, 5, 6, 8] == to_list(s.partition(head=from_list([1, 3, 5, 2, 6, 8]), x=5))
assert [1, 1, 1, 1] == to_list(s.partition(head=from_list([1, 1, 1, 1]), x=1))
