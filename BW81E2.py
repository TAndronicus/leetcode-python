from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        groups = {i: i for i in range(n)}
        for edge in edges:
            if len(groups) == 1:
                return 0
            maxGroup, minGroup = max(groups[edge[0]], groups[edge[1]]), min(groups[edge[0]], groups[edge[1]])
            if maxGroup != minGroup:
                for key, group in groups.items():
                    if group == maxGroup:
                        groups[key] = minGroup
        numberOfEl = {}
        for key, group in groups.items():
            numberOfEl[group] = numberOfEl.get(group, 0) + 1
        if len(numberOfEl) == 1:
            return 0
        else:
            prod = 0
            for group1, num1 in numberOfEl.items():
                for group2, num2 in numberOfEl.items():
                    if group1 < group2:
                        prod += (num1 * num2)
            return prod


if __name__ == '__main__':
    s = Solution()
    print(s.countPairs(3, [[0, 1], [0, 2], [1, 2]]) == 0)
    print(s.countPairs(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]) == 14)
    print(s.countPairs(11, [[5, 0], [1, 0], [10, 7], [9, 8], [7, 2], [1, 3], [0, 2], [8, 5], [4, 6], [4, 2]]) == 0)
