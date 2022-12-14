import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        fact, curr = math.factorial(n - 1), n - 1
        pool, pointer, res = list(range(n)), 0, [''] * n
        while curr != 0:
            bucket = int(k / fact)
            res[pointer] = str(pool.pop(bucket) + 1)
            k = k % fact
            fact = int(fact / curr)
            curr -= 1
            pointer += 1
        res[-1] = str(pool.pop(0) + 1)
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3, 5) == '312')
    print(s.getPermutation(3, 3) == '213')
    print(s.getPermutation(4, 9) == '2314')
    print(s.getPermutation(3, 1) == '123')
