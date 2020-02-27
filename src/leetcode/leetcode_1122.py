# 2019-7-16

class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        res = []
        not_in_arr2 = [x for x in arr1 if x in (set(arr1) - set(arr2))]
        not_in_arr2.sort()
        print(not_in_arr2)
        for x in arr2:
            cnt = 0
            for ele in arr1:
                cnt += 1 if ele == x else 0
            res.extend([x] * cnt)

        # Process tail

        res.extend(sorted(not_in_arr2))


        return res
