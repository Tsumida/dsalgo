
class Solution:
    def replaceSpace(self, s: str) -> str:
        def method_1(st:str) -> str:
            arr_str = s.split(" ")
            return "%20".join(p for p in arr_str)

        def method_2(st:str) -> str:
            res = ""
            for ch in st:
                if ch == " ":
                    res += "%20"
                else:
                    res += ch
            return res

        return method_2(s)



s = Solution()
assert s.replaceSpace(s="We are happy.") == "We%20are%20happy."
assert s.replaceSpace(s="Hello, world!") == "Hello,%20world!"
