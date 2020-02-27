# 2019-8-24

# Passed.
class Solution:
    def invalidTransactions(self, transactions:list) -> list:
        res = list()
        T_MAX_AMOUNT = 1000
        T_INT = 60

        map = dict()
        # O(n^2)
        amount_invalid = set()
        for t in transactions:
            name, time, amount, city = t.split(',')
            time = int(time)
            amount = int(amount)
            if amount > T_MAX_AMOUNT:
                amount_invalid.add(t)
            if name not in map:
                map[name] = [(time, amount, city)]
            else:
                map[name].append((time, amount, city))

        # 同名中
        for k, lis in map.items():
            same_name = set()
            for v in lis:
                time, amount, city = v
                # 找到不同城市且间隔小于60
                temp = ["{},{},{},{}".format(k, str(t), str(a), c)
                        for t, a, c in lis if abs(time - t) <= T_INT and city != c ]

                if len(temp) > 0:   # 表示有无效
                    temp.append("{},{},{},{}".format(k, str(time), str(amount), city))

                temp = set(temp)
                same_name = same_name.union(temp)
                #print("tp = ", temp)

            same_name = same_name - amount_invalid #

            #print("sn = ", same_name)
            res.extend(list(same_name))
            same_name.clear()
        #print("am = ", amount_invalid)
        res.extend(amount_invalid)
        return res

s = Solution()
print(s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]))
print(s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,30,1200,mc","alice,20,800,mkk","alice,30,1200,mg"]))
print(s.invalidTransactions(transactions = ["bob,689,1910,barcelona",   # >1000
                                            "alex,696,122,bangkok",
                                            "bob,832,1726,barcelona",   # >1000
                                            "bob,820,596,bangkok",      # diff
                                            "chalicefy,217,669,barcelona",
                                            "bob,175,221,amsterdam"]))
