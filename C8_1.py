class Solution:
    def tripleStep(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        s1, s2, s3 = 1, 2, 4
        for i in range(n - 3):
            s1, s2, s3 = s2, s3, s1 + s2 + s3
        return s3


if __name__ == '__main__':
    s = Solution()
    print(s.tripleStep(4) == 7)
    print(s.tripleStep(5) == 13)
