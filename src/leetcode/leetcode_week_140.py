# 2019-6-9

'''
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def recu(leng:int):
            nonlocal strs
            if leng <= lens:
                for i, word in enumerate(tiles):
                    if not ischosen[i]:
                        ischosen[i] = True
                        strs += word
                        sets.add(strs)
                        recu(leng+1)

                        ischosen[i] = False
                        strs = strs[:-1]




        res = 0
        sets = set()
        ischosen = [False for x in range(len(tiles))]
        lens = len(tiles)
        strs = ""

        # 深度优线：
        recu(0)

        res = len(sets)

        return res

s = Solution()
print(s.numTilePossibilities("AAABBC"))
'''

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        res = ""
        alphabet = [list() for x in range(23)]
        lenk = len(set([x for x in text]))
        


        return res
