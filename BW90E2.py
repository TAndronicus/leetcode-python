from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        for query in queries:
            for word in dictionary:
                if self.matches(word, query):
                    yield query
                    break

    def matches(self, word: str, query: str) -> bool:
        mistakes = 0
        for i in range(len(word)):
            if word[i] != query[i]:
                if mistakes < 2:
                    mistakes += 1
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(list(s.twoEditWords(["word", "note", "ants", "wood"], ["wood", "joke", "moat"])))
    print(list(s.twoEditWords(["yes"], ["not"])))
