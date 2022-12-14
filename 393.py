from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        counter = 0
        for byte in data:
            if byte & 248 == 240 and counter == 0:
                counter = 3
            elif byte & 240 == 224 and counter == 0:
                counter = 2
            elif byte & 224 == 192 and counter == 0:
                counter = 1
            elif byte & 192 == 128 and counter > 0:
                counter -= 1
            elif byte & 128 == 0 and counter == 0:
                continue
            else:
                return False
        return counter == 0


if __name__ == '__main__':
    s = Solution()
    print(s.validUtf8([197, 130, 1]))
    print(not s.validUtf8([235, 140, 4]))
