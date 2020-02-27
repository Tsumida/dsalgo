class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        def is_prime(number:int) -> bool:
            if number < 2:
                return False
            elif number == 2:
                return True
            elif number % 2 == 0:
                return False
            else:
                # 从3开始
                fac = 2
                while fac ** 2 <= number:
                    if number % fac == 0:
                        return False
                    fac += 1

                return True

        def mod_cal(number:int) -> int:
            if number < 2:
                return 1
            else:
                return (number * mod_cal(number - 1)) % (10**9 + 7)

        num_prime = 0
        for i in range(1, n+1):
            if is_prime(i):
                num_prime += 1

        res = ( mod_cal(num_prime) * mod_cal(n - num_prime) ) % (10**9 + 7)

        return res

s = Solution()
print(s.numPrimeArrangements(n=5))
print(s.numPrimeArrangements(n=100))
