import math
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        groups = {i: i for i in range(n)}
        for edge in edges:
            groups[edge[0]] = min(groups[edge[0]], groups[edge[1]])
            groups[edge[1]] = groups[edge[0]]
        numberOfEl = {}
        for key in groups.keys():
            group = groups[key]
            while group != groups[group]:
                group = groups[group]
            numberOfEl[group] = numberOfEl.get(group, 0) + 1
        if len(numberOfEl) == 1:
            return 0
        else:
            sum, sumsq = 0, 0
            for group1, num1 in numberOfEl.items():
                sum += num1
                sumsq += math.pow(num1, 2)
            return int((math.pow(sum, 2) - sumsq) / 2)


if __name__ == '__main__':
    s = Solution()
    print(s.countPairs(3, [[0, 1], [0, 2], [1, 2]]) == 0)
    print(s.countPairs(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]) == 14)
    print(s.countPairs(11, [[5, 0], [1, 0], [10, 7], [9, 8], [7, 2], [1, 3], [0, 2], [8, 5], [4, 6], [4, 2]]) == 0)
    print(s.countPairs(16, [[0, 15], [1, 14], [2, 11], [4, 3], [5, 15], [8, 2], [14, 12]]) == 110)
