from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ar = self.produceArray(n)
        cumProd = [0] * (len(ar) + 1)
        cumProd[0] = 1
        for i in range(1, len(ar) + 1):
            cumProd[i] = cumProd[i - 1] * ar[i - 1]
        for query in queries:
            yield int(cumProd[query[1] + 1] / cumProd[query[0]]) % 1000000007

    def produceArray(self, n: int):
        res = []
        pow = 1
        for ch in reversed(bin(n)[2:]):
            if ch == '1':
                res.append(pow)
            pow *= 2
        return res


if __name__ == '__main__':
    s = Solution()
    print(list(s.productQueries(15, [[0, 1], [2, 2], [0, 3]])))
    print(list(s.productQueries(2, [[0, 0]])))
    print(list(s.productQueries(11, [[0, 0], [0, 1], [1, 1], [1, 2], [0, 2]])))
