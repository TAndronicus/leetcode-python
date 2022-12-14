from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
        for el in queue:
            repr = ['.' * n] * n
            for i in range(n):
                ar = ['.'] * n
                ar[el[i]] = 'Q'
                repr[i] = ''.join(ar)
            yield repr


if __name__ == '__main__':
    s = Solution()
    print(list(s.solveNQueens(1)))
    print(list(s.solveNQueens(2)))
    print(list(s.solveNQueens(3)))
    print(list(s.solveNQueens(4)))
    print(len(list(s.solveNQueens(5))))
