from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        cache = {}
        for spell in spells:
            if spell in cache:
                yield cache[spell]
            else:
                success_spell = success / spell
                count = len(list(filter(lambda el: el >= success_spell, potions)))
                cache[spell] = count
                yield count


if __name__ == '__main__':
    s = Solution()
    print(list(s.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)) == [4, 0, 3])
    print(list(s.successfulPairs([3, 1, 2], [8, 5, 8], 16)) == [2, 0, 2])
    print(list(s.successfulPairs([1], [1], 2)) == [0])
