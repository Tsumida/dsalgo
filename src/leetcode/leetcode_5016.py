# 2019-4-7

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        """

        删除外层括号：  --> 递归 (str, left+1, right-1)
        返回空 ：      left == right ---> return ""



        :param S:
        :return:
        """
        res = ""
        left = list()
        right = list()
        # 括号匹配
        # 只存left
        left_new_start = 0  # 为新的大括号准备
        for i, quota in enumerate(S):
            if quota == '(':
                left.append(i)
            elif quota == ')' and len(left[left_new_start:]) > 1:
                left.pop()
            else:
                right.append(i) # so left, right record the index of the outest () of a primitive
                left_new_start +=1
        for i, le in enumerate(left):
            if le+1 < right[i]:
                #print(le, " ", right[i])
                res += S[le+1: right[i]] # [le+1, right(i))

        return res


    def test(self):
        test_cases = [
            ("(()())(())", "()()()"),
            ("(()())(())(()(()))", "()()()()(())"),
            ("()()", ""),
        ]

        for test in test_cases:
            arg, ans = test
            out = self.removeOuterParentheses(arg)
            print("is equal ? :", out == ans)
            #print(out)

s1 = Solution()
s1.test()
