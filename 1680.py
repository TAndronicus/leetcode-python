class Solution:
    def concatenatedBinary1(self, n: int) -> int:
        res = ""
        for i in range(n):
            res += bin(i + 1)[2:]
        return int(res, 2) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.concatenatedBinary1(1) == 1)
    print(s.concatenatedBinary1(3) == 27)
    print(s.concatenatedBinary1(12) == 505379714)
