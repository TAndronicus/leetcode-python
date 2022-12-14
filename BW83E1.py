from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return "Flush"
        ranksDict = {}
        for rank in ranks:
            if rank not in ranksDict:
                ranksDict[rank] = 1
            else:
                ranksDict[rank] += 1
        for _, rank in ranksDict.items():
            if rank >= 3:
                return "Three of a Kind"
        for _, rank in ranksDict.items():
            if rank == 2:
                return "Pair"
        return "High Card"


if __name__ == '__main__':
    s = Solution()
    print(s.bestHand([13, 2, 3, 1, 9], ["a"] * 5) == "Flush")
    print(s.bestHand([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]))
    print(s.bestHand([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"]))
