# 2019-5-20

"""
    For each asteroid,
        the absolute value represents its size,
        and the sign represents its direction
        (positive meaning right, negative meaning left).
    Each asteroid moves at the same speed.

Target:
    Find out the state of the asteroids after all collisions.

Rules:
    If two asteroids meet, the smaller one will explode.
    If both are the same size, both will explode.
    Two asteroids moving in the same direction will never meet.


"""


class Solution:
    def asteroidCollision(self, asteroids: list) -> list:
        res = list()
        for r in asteroids:
            flag = True # True --> push r;
            while len(res) > 0 and res[-1] > 0:
                if r < 0:
                    # elimination.
                    sp = res[-1]
                    abs_r = abs(r)
                    if sp < abs_r:              # eliminate sp. and push r
                        res.pop()
                    else:
                        flag = False            # sp > r eliminate r.
                        if sp == abs_r:         # eliminate sp and r.
                            res.pop()
                        break
                else: # safe
                    break
            if flag:
                res.append(r)
            #print(res)

        return res

def test():
    s = Solution()

    test_cases = [

        ([-2, -3, -6, 1, 1, 1], [-2, -3, -6, 1, 1, 1]),
        ([9, 5, 6, -3, -8, 5], [9, 5]),
        ([1, 2, 3, 4, 5, -10], [-10]),
        ([5, 10, -5], [5, 10]),
        ([10] * 100, [10]*100),
        ([-1, -2, -3, -4, 5, 8, -7], [-1, -2, -3, -4, 5, 8]),
        ([8, -8], []),
    ]

    for i, t in enumerate(test_cases):
        inp, ans = t
        out = s.asteroidCollision(inp)
        if out == ans:
            print(f"Test-{i} passed.")
        else:
            print(f"Test-{i} failed. Output={out}, answer={ans}")
    print("Done.")

test()
