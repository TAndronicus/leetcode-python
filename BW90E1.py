from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        firstAr = None
        secondAr = None
        dupl = False
        for word in words:
            ar = [0] * (len(word) - 1)
            for i in range(len(word) - 1):
                ar[i] = ord(word[i + 1]) - ord(word[i])
            if firstAr is None:
                firstAr = (ar, word)
            elif firstAr[0] != ar:
                if dupl:
                    if secondAr is None:
                        return word
                    else:
                        return firstAr[1]
                if secondAr is None:
                    secondAr = (ar, word)
                else:
                    return firstAr[1]
            else:
                if secondAr is None:
                    dupl = True
                else:
                    return secondAr[1]
        return ''


if __name__ == '__main__':
    s = Solution()
    print(s.oddString(["adc", "wzy", "abc"]))
    print(s.oddString(["aaa", "bob", "ccc", "ddd"]))
