class Solution:
    def totalNQueens(self, n: int) -> int:
        queue = [[]]
        for i in range(n):
            newQueue = []
            for el in queue:
                for j in range(n):
                    beats = False
                    for k in range(len(el)):
                        if el[-(k + 1)] == j + (k + 1) or el[-(k + 1)] == j - (k + 1):
                            beats = True
                            break
                    if j in el or beats:
                        continue
                    newQueue = newQueue + [el + [j]]
            queue = newQueue
        return len(queue)


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(1))
    print(s.totalNQueens(2))
    print(s.totalNQueens(3))
    print(s.totalNQueens(4))
    print(s.totalNQueens(5))
