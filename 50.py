import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or (x == -1 and n % 2 == 0):
            return 1
        elif x == -1:
            return -1
        elif x == 0:
            return 0
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        if n < 0:
            n, x = -n, 1 / x
        log = int(math.log2(n))
        pows = [x] * (log + 1)
        for i in range(1, log + 1):
            pows[i] = pows[i - 1] * pows[i - 1]
        prod = 1
        while n > 0:
            pow_2 = math.pow(2, log)
            if n >= pow_2:
                prod *= pows[log]
                n -= pow_2
            log -= 1
        return prod


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2, 4))
    print(s.myPow(-2, 4))
    print(s.myPow(-2, 3))
    print(s.myPow(.2, 4))
