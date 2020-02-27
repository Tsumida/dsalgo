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

# 链表有多少个分量
class Solution:
    def numComponents(self, head: ListNode, G: list):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """

        res = 0
        set_g = set(G)
        p = head
        in_component = False
        while p:
            if p.val in set_g:
                in_component = True
            else:
                if in_component : # 表示之前是在component中， 现在不在， 要
                    res += 1
                in_component = False

            p = p.next
        # 如[0, 1, 2, 3, 4] G = [0, 3, 1, 4]
        # 检查末尾
        if in_component:
            res += 1
        #print("--"*5, res)
        return res

s = Solution()
assert 2 == s.numComponents(head=from_list([0, 1, 2, 3, 4]), G=[0, 3, 1, 4])
assert 1 == s.numComponents(head=from_list([0, 1, 3, 3, 4]), G=[0, 3, 1, 4])
assert 2 == s.numComponents(head=from_list([6, 1, 7, 5, 4]), G=[0, 3, 1, 4])
assert 0 == s.numComponents(head=from_list([6, 1, 7, 5, 4]), G=[0, 3, 3, 3])
assert 3 == s.numComponents(head=from_list([0,1,2,3, 9, 9, 9, 9, 10, 7]), G=[0,1,3,7])
