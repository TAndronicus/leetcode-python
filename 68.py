import math
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        while len(words) > 0:
            row = [words.pop(0)]
            length = len(row[0])
            while len(words) > 0 and length + len(words[0]) + 1 <= maxWidth:
                row.append(words.pop(0))
                length += (len(row[-1]) + 1)
            if len(words) == 0 or len(row) == 1:
                res.append(' '.join(row) + (' ' * (maxWidth - length)))
            else:
                rowStr = row.pop(0)
                rowLen = len(row)
                remainingLength = length - (rowLen + len(rowStr))
                for i in range(rowLen):
                    numOfSpaces = math.ceil((maxWidth - len(rowStr) - remainingLength) / len(row))
                    remainingLength -= len(row[0])
                    rowStr += (' ' * numOfSpaces + row.pop(0))
                res.append(rowStr)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fullJustify(['a'], 4) == ['a   '])
    print(s.fullJustify(['a', 'aaa'], 4) == ['a   ', 'aaa '])
    print(s.fullJustify(['a', 'a', 'a'], 4) == ['a  a', 'a   '])
    print(s.fullJustify(['a', 'aaaa', 'a'], 4) == ['a   ', 'aaaa', 'a   '])
    print(s.fullJustify(['a', 'a', 'aaaa', 'a', 'a'], 4) == ['a  a', 'aaaa', 'a a '])
    print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == ["This    is    an", "example  of text",
                                                                                                 "justification.  "])
    print(s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == ["What   must   be", "acknowledgment  ", "shall be        "])
    print(s.fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
         "we", "do"], 20) ==
          ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we",
           "do                  "])
