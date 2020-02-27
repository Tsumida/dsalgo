class CQueue:

    def __init__(self):
        self.left_st = list()
        self.right_st = list()

    def appendTail(self, value: int) -> None:
        self.right_st.append(value)

    def deleteHead(self) -> int:
        # print(self.left_st, self.right_st)
        n, m = len(self.left_st),len(self.right_st)
        if n == 0 and m == 0:
            return -1
        if n > 0:
            return self.left_st.pop()
        # m > 0
        for ele in reversed(self.right_st):
            self.left_st.append(ele)
        self.right_st.clear()
        return self.left_st.pop()


lis = [1, 2, 3, 4, 5, 6, 7]
cq = CQueue()
assert -1 == cq.deleteHead()
for i in lis:
    cq.appendTail(i)

assert 1 == cq.deleteHead()
assert 2 == cq.deleteHead()
assert 3 == cq.deleteHead()
assert 4 == cq.deleteHead()
assert 5 == cq.deleteHead()
assert 6 == cq.deleteHead()
assert 7 == cq.deleteHead()
assert -1 == cq.deleteHead()
