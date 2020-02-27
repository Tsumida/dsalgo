# 2019-5-19

class Solution:
    '''
    def removeDuplicates(self, S: str) -> str:
        """
        T(n) = O(n^2)
        :param S:
        :return:
        """
        def split(S:str, a:int, b:int) -> str:
            # [a, b)
            res = ""
            if a+1 == b:
                res = S[a]
            elif a+1 < b:
                mid = (a+b) // 2
                astr = split(S, a, mid)
                bstr = split(S, mid, b)
                if astr == "" or bstr == "":
                    res = astr + bstr
                else:
                    #res = astr+bstr
                    #temp = reversed(astr)
                    i, j = len(astr)-1, 0
                    while i >= 0 and j < len(bstr) \
                                 and astr[i] == bstr[j]:
                        i, j = i-1, j+1
                    res = astr[0:i+1] + bstr[j:]

            #print("a={}. b={}, res={}".format(a, b, res))

            return res

        return split(S, 0, len(S))
    '''

    def removeDuplicates(self, S: str) -> str:
        """
        Stack operation. O(n)

        :param S:
        :return:
        """

        st = list()
        res = ""

        for char in S:
            # Empty stack, push.
            if len(st) == 0 or st[-1] != char:
                st.append(char)
            else:
                st.pop()
        #print("St: ", st)
        res = "".join(st)

        return res



s1 = Solution()
test_cases = [
    "abcabc", # abcabc
    "abbaca", # ca
    "aaaaaa", # ""
    "aba" * 5, # ""
]

for i, t in enumerate(test_cases):
    #print("0123456")
    print("i=", i, s1.removeDuplicates(t))
