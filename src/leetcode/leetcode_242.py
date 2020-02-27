# 2018-11-18

import testFunctions as tf

class Solution:


    def isAnagram(self, s, t):
        res = True
        alphabet_keys = 'abcdefghijklmnopqrstuvwxyz'
        # alphabet_vals = [True for i in range(52)]

        alphabet_map_s = dict.fromkeys(alphabet_keys, 0)
        alphabet_map_t = dict.fromkeys(alphabet_keys, 0)

        for ts in s:
            alphabet_map_s[ts] += 1
        for ts in t:
            alphabet_map_t[ts] += 1



        for ts in alphabet_keys:
            # print(alphabet_map_s[ts],'---', alphabet_map_t[ts])
            if alphabet_map_t[ts] != alphabet_map_s[ts]:
                res = False

        return res

@tf.timer
def test(time):
    s1 = Solution()
    s = 'aaaabasdadasdsadadsasa'
    t = 'aaaacsadsadsadsadasdsawqeq'

    for i in range(time):
        s1.isAnagram(s, t)
    return True




if __name__ == '__main__':
    test(100000)
