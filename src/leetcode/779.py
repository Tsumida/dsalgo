

"""
12345678..
0
01
0110
01101001
0110100110010110
01101001100101101001011001101001

"""
class Solution:

    def kthGrammar(self, N: int, K: int) -> int:
        # f(1, 1) = "0"
        # f(N, K) =  f(N-1, K // 2) , K % 2 == 1
        #         = ~f(N-1, K // 2) , K % 2 == 0
        print(f"N = {N}, K = {K}")
        if N <= 1 or K <= 1:
            return 0
        else:
            #  f(N+1, 2K-1) = f(N, K)
            # ~f(N+1, 2K  ) =
            if K % 2 == 1:
                return self.kthGrammar(N-1, (K+1) // 2)
            else:
                return 1 if self.kthGrammar(N-1, K // 2) == 0 else 0

s = Solution()
test_cases = [
    (1, 1, 0),
    (2, 1, 0),
    (2, 1, 0),
    (4, 3, 1),
    (6, 12, 1),
    (10, 1024, 1),
]

num_failed_indices = list()

for i, case in enumerate(test_cases):
    N, K, ans = case
    out = s.kthGrammar(N, K)
    try :
        assert ans == out
    except AssertionError:
        num_failed_indices.append((i, out, case))
    #print(f"index = {i}\t ans = {ans}\t output = {out} for args = (N={N}, K={K})")

print("Tests failed:\n",
      "\n".join(f"index = {i}\targs = {case} while output = {out}"
                        for i, out, case in num_failed_indices))

