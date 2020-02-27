# 2019-9-8

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        def is_leap_year(yea: int) -> bool:
            # 1971 <= yea <= 2100, 只有2000是世纪闰年
            return yea % 4 == 0

        res = ""
        maps = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


        nor_months = [31, 28,31,30,31,30,31,31,30,31,30,31]
        leap_months = [31, 29,31,30,31,30,31,31,30,31,30,31]
        nor_sums = sum(nor_months)
        leap_sums = nor_sums + 1


        first_day_index = 5 # 1971年1月1日是 星期五， 对应index = 5
        for i in range(1971, year):
            # i年是否闰年
            if is_leap_year(i): # 加上这一年         ===================================================== !
                first_day_index = (first_day_index + leap_sums) % 7
            else:
                first_day_index = (first_day_index + nor_sums) % 7
            # 此时的 first_day_index 表示的是 i + 1 年1月1日是星期几
            print(i+1, first_day_index, is_leap_year(i+1))

        # 处理 year
        # [:month - 1] 这里容易出错，
        # 比如我们要算 8月3日, 那么要计算1-7月有多少天， 也就是 [0, 7) 对应就是 [0, month - 1)    ============= !
        m_sums =  sum(leap_months[:month-1]) if is_leap_year(year) \
                                             else sum(nor_months[:month-1])
        # 如 1971 2月3日为：
        # 5  + 31 + 3 - 1 = 38 % 7 = 3 ==> 星期三
        first_day_index = (first_day_index + m_sums + day - 1) % 7  # ===================================== !
        print(m_sums, first_day_index)
        res = maps[first_day_index]


        return res
