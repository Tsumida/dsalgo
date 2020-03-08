class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        hmap = dict()
        for ch in s:
            if ch not in hmap:
                hmap[ch] = 1
            else:
                hmap[ch] += 1
        ch_set = list(set(s))
        ch_set.sort()
        c = len(s)
        while c > 0:
            for ch in ch_set:
                cnt = hmap[ch]
                if cnt > 0:
                    hmap[ch] -= 1
                    res += ch
                    c -= 1

            for ch in reversed(ch_set):
                cnt = hmap[ch]
                if cnt > 0:
                    hmap[ch] -= 1
                    res += ch
                    c -= 1

        return res

s = Solution()
assert "abccbaabccba" == s.sortString(s="aaaabbbbcccc")
assert "art" == s.sortString(s="rat")
