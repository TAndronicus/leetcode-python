from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        queue = [[]]
        elements = dict()
        for i in candidates:
            elements[i] = elements.get(i, 0) + 1
        for element, max_cnt in elements.items():
            newQueue = []
            for el in queue:
                cnt = (target - sum(el)) / element
                newQueue = newQueue + [el + ([element] * i) for i in range(min(int(cnt), max_cnt) + 1)]
            queue = newQueue
        for el in queue:
            if sum(el) == target:
                yield el


if __name__ == '__main__':
    s = Solution()
    print(list(s.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)))
    print(list(s.combinationSum([2, 5, 2, 1, 2], 5)))
