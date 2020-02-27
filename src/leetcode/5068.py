# 2019-9-7


'''
    「短语」（phrase）是仅由小写英文字母和空格组成的字符串。
    「短语」的开头和结尾都不会出现空格，「短语」中的空格不会连续出现。
    「前后拼接」（Before and After puzzles）是合并两个「短语」形成「新短语」的方法。
     我们规定拼接时，第一个短语的最后一个单词 和 第二个短语的第一个单词 必须相同。
'''

class Solution:
    def beforeAndAfterPuzzles(self, phrases: list) -> list:
        res = list()
        # 对每个ph in phrases， 记录其prex和post
        # 对每个ph, 按照其end， 与每个ph' with post' == end做笛卡尔积, 产生结果； 不能和自己笛卡尔积
        pre_post = list()
        for ph in phrases:
            tmp = list()
            tmp.append(ph.split(" ", 1)[0])     # 空或非空
            tmp.append(ph.rsplit(" ", 1)[-1])
            pre_post.append(tmp)

        print("pp = ", pre_post)

        for i, tmp_x in enumerate(pre_post):
            for j, tmp_y in enumerate(pre_post):
                if len(tmp_x[1]) * len(tmp_y[0]) <= 0:
                    pass # 不用做拼接
                if i != j and tmp_x[1] == tmp_y[0]:
                    #
                    # 假定pre, post都是非空
                    if phrases[i] == phrases[j]:
                        res.append(phrases[i])
                    else:
                        left = phrases[i].rsplit(tmp_x[1], 1)[0]
                        right = phrases[j]
                        t1 = left + right
                    #print(t1)
                        print("-{}\n--{}\n---{}".format(t1, left, right))
                        res.append(
                            t1
                        )
        res = list(set(res))
        res.sort()
        print(res)

        return res



s = Solution()

assert ["writing code rocks"] == s.beforeAndAfterPuzzles(phrases=["writing code","code rocks"])

assert sorted(["a chip off the old block party",
      "a man on a mission impossible",
      "a man on a mission statement",
      "a quick bite to eat my words",
      "chocolate bar of soap"]) == \
       sorted(s.beforeAndAfterPuzzles(phrases=["mission statement",
                "a quick bite to eat",
                "a chip off the old block",
                "chocolate bar",
                "mission impossible",
                "a man on a mission",
                "block party",
                "eat my words",
                "bar of soap"]))

assert ["a"] == s.beforeAndAfterPuzzles(phrases=["a","b","a"])

assert ["ggwznmv twecfm nrop nrop nrop xshcva ggwznmv ggwznmv p twecfm nrop xshcva p p p nrop ggwznmv twecfm nrop p p","xshcva twecfm ggwznmv twecfm nrop p ggwznmv p twecfm"]         == s.beforeAndAfterPuzzles(
            phrases=["nrop xshcva twecfm twecfm twecfm xshcva twecfm","ggwznmv twecfm nrop nrop nrop xshcva ggwznmv ggwznmv p twecfm nrop xshcva p p","p p nrop ggwznmv twecfm nrop p p","xshcva twecfm ggwznmv twecfm nrop p ggwznmv p twecfm","xshcva"]
            )
