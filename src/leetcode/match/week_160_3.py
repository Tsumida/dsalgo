# 2019-10-27

'''
给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，
如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
请返回所有可行解 s 中最长长度。

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] 中只含有小写英文字母

1. 两个字符串之间是正交的
2. 字符串自身的字符是正交的
3. 如果一个字符串自身不是正交的， 不用考虑它

'''

class Solution:
    def maxLength(self, arr: list) -> int:
        # arr[i] 本身的字符也要是不重复!
        res = 0
        n = len(arr)

        is_unique = [False for _ in range(n)]
        for i, a in enumerate(arr):
            p = len(set(c for c in a))
            if p == len(a):
                is_unique[i] = True
                res = max(res, p)

        # 如果交集为空, 则是合法
        table = [set(c for c in word) for word in arr]
        cate = [[i] for i in range(n)]
        for i in range(n):
            tmp = table[i].copy()
            # self is not unique. break
            if not is_unique[i]:
                continue
            for j in range(n):
                if not is_unique[j]:
                    continue
                flag = False
                # O(1)
                for c in arr[j]:
                    if c in tmp:
                        flag = True
                        break
                if not flag:
                    tmp.update(c for c in arr[j])
            res = max(res, len(tmp))

        print(res)
        return res

s = Solution()

assert 4 == s.maxLength(arr= ["un","iq","ue"])
assert 6 == s.maxLength(arr = ["cha","r","act","ers"])
assert 26 == s.maxLength(arr =["abcdefghijklmnopqrstuvwxyz"])
assert 16 == s.maxLength(arr=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"])
assert 0 == s.maxLength(arr=["yy", "bkhwmpbiisbldzknpm"])

assert 1 == s.maxLength(arr=["e","tpgynpylqbyqjaf","svkgfmpgftxjjrcxxsog","bxypbbrlckiolfwpqgsoc","kwnelumrnnsryjdeppanuqbsu"])
