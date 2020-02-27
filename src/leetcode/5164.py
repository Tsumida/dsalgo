# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None


def fromlist(lis:list) -> ListNode:
    res = ListNode(0)
    if len(lis) > 0:
        res.next = ListNode(lis[0])
        tail = res.next
        for ele in lis[1:]:
            tail.next = ListNode(ele)
            tail = tail.next

    return res.next

def tolist(head:ListNode) -> list:
    res = list()
    t = head
    while t:
        res.append(t.val)
        t = t.next

    return res

def get_vals(h: ListNode) -> list:
    lis = list()
    t = h
    while t:
        lis.append(t.val)
        t = t.next
    #print("get_vals() ", lis)
    return lis

def cal_acc(vals:list):
    list_val = vals.copy()
    for i in range(1, len(list_val)):
        list_val[i] += list_val[i-1]
    #print("cal_acc() ",list_val)
    return list_val


class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:



        res = head
        vals = get_vals(res)
        end_loop = False
        while not end_loop:
            acc = cal_acc(vals)

            #print("vals ", vals)
            #print("acc  ", acc)

            hmap = dict()
            # 用哈希表计算出最长子串
            for i, ss in enumerate(acc):
                if ss not in hmap:
                    hmap[ss] = [i]
                else:
                    hmap[ss].append(i)

            max_dis = 0
            st, end = -1, -1
            for ins in hmap.values():
                if len(ins) >= 1:
                    s, e = min(ins), max(ins)
                    if max_dis < e - s :
                        st, end = s, e
                        max_dis = e - s

            if st == -1 and end == -1:  # 终止
                end_loop = True
            else:
                # deletion (st, end]
                #print(f"st = {st}, end = {end}")
                if end < len(vals) - 1:
                    vals = vals[:st+1] + vals[end+1:]
                else:
                    vals = vals[:st+1]
        # 看看vals里面有没有0的
        acce = cal_acc(vals)
        end = -1
        for i, s in enumerate(acce):
            if s == 0:
                end = i # 从所有0中找到最大下标的
        if end >= 0:
            vals = vals[end+1:]



        # rebuild list form vals.
        return fromlist(vals)


s = Solution()
#tests = [1,2,-3,3,1]
#tests = [1,2,3,-3,-2]
#tests = [1,2,3,-3,4] + [3,-3] * 1
tests = [0, 0, 0, 0]  # ---------------- [0] 错误
#tests = [1, 1, -1, -1] # ---------------- [1, -1] 错误
lis = fromlist(tests)
print(tolist(lis))
print(tolist(s.removeZeroSumSublists(head=lis)))
#s.removeZeroSumSublists(head=lis)
