
# Passed.
class Solution:
    def numSmallerByFrequency(self, queries: list, words: list) -> list:

        def calculas(s:str) -> int:
            ans = 0
            fre = [0 for x in range(26)]
            for ch in s:
                fre[ord(ch) - ord('a')] += 1
            for f in fre:
                if f > 0:
                    ans = f
                    break

            return ans

        res = list()
        f_w = [calculas(strs) for strs in words]
        for i, q in enumerate(queries):
            cmp = f_w[i]
            f_q = calculas(q)
            tmp_res = sum(1 for fw in f_w if fw > f_q)
            res.append(tmp_res)

        return res

s = Solution()
print(s.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"])) # [1]
print(s.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])) #[1, 2]
