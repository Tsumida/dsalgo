

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        '''
                0 1 2 3 4
            0
            1
            2

        :param target:
        :return:
        '''
        def get_delta(start_row:int, start_col:int, target):

            t_r, t_c = target // 5, target % 5
            return (t_r - start_row, t_c - start_col)


        res = ""

        # 要按顺序遍历每个target每个字母
        # 两点之间最短距离为曼哈顿距离
        lens = len(target)
        # 返回两地之间的坐标差，来决定路径
        now_row, now_col = 0, 0
        for ch in target:


            #print("ch = ", ch, ord(ch)-97, delta_r, delta_c)
            now_ch = chr( now_row * 5 + now_col + 97)
            is_u_to_z = False # 用来表示终点是否是z
            #while now_ch != ch:
            temp = ""
            # 起点终点都不是'z'
            if ch == 'z' and now_ch == 'z':
                pass
            elif now_ch == 'z': # 出去就好了
                temp += "U"
                now_ch = 'u'
                now_row -= 1
            elif ch == 'z':
                is_u_to_z = True
                ch = 'u' # 先到u


            delta_r, delta_c = get_delta(now_row, now_col,ord(ch)-97)

            if delta_r < 0: # 向上
                temp += "".join("U" for x in range(abs(delta_r)))
            elif delta_r > 0:
                temp += "".join("D" for x in range(delta_r))

            if delta_c < 0:
                temp += "".join("L" for x in range(abs(delta_c)))
            elif delta_c > 0:
                temp += "".join("R" for x in range(delta_c))

            if is_u_to_z:
                temp += "D" # 从u到z
                now_ch = 'z'
                now_row += 1

            now_row += delta_r
            now_col += delta_c

            temp += "!"
            res += temp



        return res

print(Solution().alphabetBoardPath(target = "leet"))
print(Solution().alphabetBoardPath(target = "zb"))
print(Solution().alphabetBoardPath(target="zezezezez"))
print(Solution().alphabetBoardPath(target="zz")) # DDDDD!!
