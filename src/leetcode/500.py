# 2019-10-26

class Solution:
    def findWords(self, words: list) -> list:
        res = list()
        new_words = [word.lower() for word in words]
        t1 = dict.fromkeys([c for c in "qwertyuiop"], 0)
        t2 = dict.fromkeys([c for c in "asdfghjkl"], 1)
        t3 = dict.fromkeys([c for c in "zxcvbnm"], 2)
        table = dict()
        table.update(t1)
        table.update(t2)
        table.update(t3)

        for i, word in enumerate(new_words):
            if len(word) > 0:
                p = table[word[0]]
                if all(p == table[ch] for ch in word):
                    res.append(words[i])


        #print(res)
        return res

s = Solution()
assert ["Alaska", "Dad"] ==  s.findWords(words=["Hello", "Alaska", "Dad", "Peace"])
assert [] == s.findWords(words=[])
assert [] == s.findWords(words=["abY", "dEf", "Abu"])
