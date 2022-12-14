from typing import List


class Solution:

    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        sets = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if j in sets:
                        sets[j].append(i)
                    else:
                        sets[j] = [i]
        for i in range(len(mat[0])):
            if i not in sets:
                sets[i] = []
        sets = list(sets.values())
        union = set()
        for _ in range(len(mat[0]) - cols):
            s = min(sets, key=lambda s: len(union.union(s)))
            sets.remove(s)
            union = union.union(s)
        return len(mat) - len(union)


if __name__ == '__main__':
    s = Solution()
    # print(s.maximumRows([[0,0,0],[1,0,1],[0,1,1],[0,0,1]], 2) == 3)
    # print(s.maximumRows([[1],[0]], 1) == 2)
    # print(s.maximumRows([[0, 0, 1],[1, 0, 0], [0, 0, 0]], 2) == 3)
    # print(s.maximumRows([[0,0,1,0,1],[0,1,0,0,1],[1,0,1,1,1],[1,0,0,0,0],[1,1,1,1,1],[0,1,1,0,0]], 1) == 1)
    print(s.maximumRows([[0, 0, 1, 0, 1], [0, 1, 0, 0, 1], [1, 0, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 0, 0]], 1))
