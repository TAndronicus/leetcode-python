from typing import List


class Solution:
    def combinationSumTailrec(self, candidates: List[int], queue: List[List[int]], target: int) -> List[List[int]]:
        if len(candidates) == 1:
            for el in queue:
                count = (target - sum(el)) / candidates[0]
                if count == int(count):
                    yield el + ([candidates[0]] * int(count))
        else:
            newQueue = []
            for el in queue:
                count = (target - sum(el)) / candidates[-1]
                newQueue = newQueue + [el + ([candidates[-1]] * i) for i in range(int(count))]
            return self.combinationSumTailrec(candidates[:-1], newQueue, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSumTailrec(candidates, [[]], target)


class SolutionLoop:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        queue = [[]]
        for candidate in reversed(candidates[1:]):
            newQueue = []
            for el in queue:
                count = (target - sum(el)) / candidate
                newQueue = newQueue + [el + ([candidate] * i) for i in range(int(count) + 1)]
            queue = newQueue
        for el in queue:
            count = (target - sum(el)) / candidates[0]
            if count == int(count):
                yield el + ([candidates[0]] * int(count))


if __name__ == '__main__':
    s = Solution()
    print(list(s.combinationSum([2, 3, 6, 7], 7)))  # not calling recursive function?
    sl = SolutionLoop()
    print(list(sl.combinationSum([2, 3, 6, 7], 7)))
    print(list(sl.combinationSum([2, 3, 5], 8)))
    print(list(sl.combinationSum([2], 1)))
