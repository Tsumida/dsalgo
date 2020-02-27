# 2019-10-19

# BF: 每个str 与其他字符串做前缀匹配， 如果某个串是str的前缀， 则去掉str
# 对于


# 考虑 /a与 /a/b
# /a/b, /a/bc
class Node:
    def __init__(self, index:int , s:str, cate: int):
        self.index = index
        self.string = s
        self.cate = cate


class Solution:
    def removeSubfolders(self, folder: list) -> list:
        '''
         root_a
         sub folders of a
         root_b
         sub folders of b
         ...


        :param folder:
        :return:
        '''
        res = list()
        folder.sort()
        #print("folder = \n", folder)
        if len(folder) > 0:
            root = folder[0]
            res.append(root)
            for p in folder[1:]:
                # /a, /a/b
                # /a, /ab
                if p.startswith(root):
                    if p[len(root)] != '/':
                        root = p
                        res.append(root)
                else:
                    root = p
                    res.append(root)



        #print(res)

        return res



s = Solution()
print(s.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))
# ["/a","/c/d","/c/f"]

print(s.removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"]))
# ["/a"]

print(s.removeSubfolders(folder = ["/a/b/c","/a/b/d","/a/b/ca"]))
# ["/a/b/c","/a/b/ca","/a/b/d"]

print(s.removeSubfolders(folder=["/a", "/a/b", "/a/bc", "/a/b/c", "/a/b/c/d"]))
# ["/a"]

print(s.removeSubfolders(folder=["/ap/ax/ay","/ap/aq/au","/aa/ab/af","/aa/ai/am","/ap/ax","/ap/aq/ar"]))
# ["/aa/ab/af","/aa/ai/am","/ap/aq/ar","/ap/aq/au","/ap/ax"]

print(s.removeSubfolders(folder=["/a","/a/b/c","/a/b/d"]))
# ["/a"\

print(s.removeSubfolders(folder=["/aa/ab/ac/ae","/aa/ab/af/ag","/ap/aq/ar/as","/ap/aq/ar","/ap/ax/ay/az","/ap","/ap/aq/ar/at","/aa/ab/af/ah","/aa/ai/aj/ak","/aa/ai/am/ao"]))
# ["/aa/ab/ac/ae","/aa/ab/af/ag","/aa/ab/af/ah","/aa/ai/aj/ak","/aa/ai/am/ao","/ap"]
