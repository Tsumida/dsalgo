# 2019-10-26

class Solution:
    def frequencySort(self, s: str) -> str:
        # 大小写
        # 按字符
        other_type = set(s)
        table = dict.fromkeys(
            [ch for ch in other_type], 0
        )

        for ch in s:
            table[ch] += 1

        tmp = [(k, v) for k, v in table.items()]
        tmp.sort(key=lambda item: item[1], reverse=True)
        res = "".join("".join(k * v for k, v in tmp))

        return res

s = Solution()
print(s.frequencySort(s="tree")) # eert / eetr
print(s.frequencySort(s="cccaa")) # cccaa
print(s.frequencySort(s="abcdefg")) # abcdefg
print(s.frequencySort(s="AaAaAaa")) # aaaaAAA
print(s.frequencySort(s="22223333333ashd")) # aaaaAAA

